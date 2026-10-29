from typing import Any

from exceptions import InvalidInputError, MemberNotFoundError
from storage import load_data, save_data
from validator import validate_text


class Member:
    """Represent a library member."""

    def __init__(
        self,
        member_id: str,
        name: str,
        active: bool = True,
    ) -> None:
        """Initialize a member."""
        self.member_id = validate_text(member_id, "Member ID")
        self.name = validate_text(name, "Member name")

        if not isinstance(active, bool):
            raise InvalidInputError(
                "Active status must be True or False."
            )

        self.active = active

    def to_dict(self) -> dict[str, Any]:
        """Convert member details to a dictionary."""
        return {
            "member_id": self.member_id,
            "name": self.name,
            "active": self.active,
        }


class MemberManager:
    """Manage library member records."""

    FILE_NAME = "members.json"

    def __init__(self) -> None:
        """Load member records."""
        self.members = load_data(self.FILE_NAME)

    def register_member(self, member: Member) -> None:
        """Register a new member."""
        if any(
            item["member_id"] == member.member_id
            for item in self.members
        ):
            raise InvalidInputError("Member ID already exists.")

        self.members.append(member.to_dict())
        save_data(self.FILE_NAME, self.members)

    def search_member(self, member_id: str) -> dict[str, Any]:
        """Find a member using their ID."""
        member_id = validate_text(member_id, "Member ID")

        for member in self.members:
            if member["member_id"] == member_id:
                return member

        raise MemberNotFoundError(
            f"Member {member_id} was not found."
        )

    def validate_membership(self, member_id: str) -> bool:
        """Check whether a member has active membership."""
        member = self.search_member(member_id)
        return member["active"] is True

    def update_member(self, member_id: str, name: str) -> None:
        """Update a member's name."""
        member = self.search_member(member_id)
        member["name"] = validate_text(name, "Member name")
        save_data(self.FILE_NAME, self.members)

    def delete_member(self, member_id: str) -> None:
        """Delete a member if they have no active book issues."""
        member_id = validate_text(member_id, "Member ID")
        member = self.search_member(member_id)

        issues = load_data("issues.json")

        active_issues = [
            issue
            for issue in issues
            if issue["member_id"] == member_id
            and issue["return_date"] is None
        ]

        if active_issues:
            raise InvalidInputError(
                "Cannot delete a member who has borrowed books."
            )

        self.members.remove(member)
        save_data(self.FILE_NAME, self.members)

    def list_members(self) -> list[dict[str, Any]]:
        """Return all members."""
        return self.members