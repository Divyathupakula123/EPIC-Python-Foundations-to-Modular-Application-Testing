import pytest

from member import Member
from exceptions import InvalidInputError


def test_create_member():
    member = Member("M101", "Divya")

    assert member.member_id == "M101"
    assert member.name == "Divya"
    assert member.active is True


def test_member_to_dict():
    member = Member("M102", "Ravi")

    assert member.to_dict() == {
        "member_id": "M102",
        "name": "Ravi",
        "active": True,
    }


def test_member_rejects_empty_name():
    with pytest.raises(ValueError):
        Member("M103", "   ")


def test_member_rejects_invalid_active_status():
    with pytest.raises(InvalidInputError):
        Member("M104", "Divya", active="yes")