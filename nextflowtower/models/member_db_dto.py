from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.org_role import OrgRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberDbDto")


@attr.s(auto_attribs=True)
class MemberDbDto:
    """
    Attributes:
        email (Union[Unset, str]):
        user_name (Union[Unset, str]):
        member_id (Union[Unset, int]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        avatar (Union[Unset, str]):
        role (Union[Unset, OrgRole]):
    """

    email: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    avatar: Union[Unset, str] = UNSET
    role: Union[Unset, OrgRole] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email
        user_name = self.user_name
        member_id = self.member_id
        first_name = self.first_name
        last_name = self.last_name
        avatar = self.avatar
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if member_id is not UNSET:
            field_dict["memberId"] = member_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email", UNSET)

        user_name = d.pop("userName", UNSET)

        member_id = d.pop("memberId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        avatar = d.pop("avatar", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, OrgRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = OrgRole(_role)

        member_db_dto = cls(
            email=email,
            user_name=user_name,
            member_id=member_id,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
            role=role,
        )

        member_db_dto.additional_properties = d
        return member_db_dto

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
