from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.org_role import OrgRole
from ..models.participant_type import ParticipantType
from ..models.wsp_role import WspRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ParticipantDbDto")


@attr.s(auto_attribs=True)
class ParticipantDbDto:
    """
    Attributes:
        type (Union[Unset, ParticipantType]):
        email (Union[Unset, str]):
        user_name (Union[Unset, str]):
        member_id (Union[Unset, int]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        participant_id (Union[Unset, int]):
        org_role (Union[Unset, OrgRole]):
        team_id (Union[Unset, int]):
        team_name (Union[Unset, str]):
        wsp_role (Union[Unset, WspRole]):
        team_avatar_url (Union[Unset, str]):
        user_avatar_url (Union[Unset, str]):
    """

    type: Union[Unset, ParticipantType] = UNSET
    email: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    member_id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    participant_id: Union[Unset, int] = UNSET
    org_role: Union[Unset, OrgRole] = UNSET
    team_id: Union[Unset, int] = UNSET
    team_name: Union[Unset, str] = UNSET
    wsp_role: Union[Unset, WspRole] = UNSET
    team_avatar_url: Union[Unset, str] = UNSET
    user_avatar_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        email = self.email
        user_name = self.user_name
        member_id = self.member_id
        first_name = self.first_name
        last_name = self.last_name
        participant_id = self.participant_id
        org_role: Union[Unset, str] = UNSET
        if not isinstance(self.org_role, Unset):
            org_role = self.org_role.value

        team_id = self.team_id
        team_name = self.team_name
        wsp_role: Union[Unset, str] = UNSET
        if not isinstance(self.wsp_role, Unset):
            wsp_role = self.wsp_role.value

        team_avatar_url = self.team_avatar_url
        user_avatar_url = self.user_avatar_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
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
        if participant_id is not UNSET:
            field_dict["participantId"] = participant_id
        if org_role is not UNSET:
            field_dict["orgRole"] = org_role
        if team_id is not UNSET:
            field_dict["teamId"] = team_id
        if team_name is not UNSET:
            field_dict["teamName"] = team_name
        if wsp_role is not UNSET:
            field_dict["wspRole"] = wsp_role
        if team_avatar_url is not UNSET:
            field_dict["teamAvatarUrl"] = team_avatar_url
        if user_avatar_url is not UNSET:
            field_dict["userAvatarUrl"] = user_avatar_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, ParticipantType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ParticipantType(_type)

        email = d.pop("email", UNSET)

        user_name = d.pop("userName", UNSET)

        member_id = d.pop("memberId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        participant_id = d.pop("participantId", UNSET)

        _org_role = d.pop("orgRole", UNSET)
        org_role: Union[Unset, OrgRole]
        if isinstance(_org_role, Unset):
            org_role = UNSET
        else:
            org_role = OrgRole(_org_role)

        team_id = d.pop("teamId", UNSET)

        team_name = d.pop("teamName", UNSET)

        _wsp_role = d.pop("wspRole", UNSET)
        wsp_role: Union[Unset, WspRole]
        if isinstance(_wsp_role, Unset):
            wsp_role = UNSET
        else:
            wsp_role = WspRole(_wsp_role)

        team_avatar_url = d.pop("teamAvatarUrl", UNSET)

        user_avatar_url = d.pop("userAvatarUrl", UNSET)

        participant_db_dto = cls(
            type=type,
            email=email,
            user_name=user_name,
            member_id=member_id,
            first_name=first_name,
            last_name=last_name,
            participant_id=participant_id,
            org_role=org_role,
            team_id=team_id,
            team_name=team_name,
            wsp_role=wsp_role,
            team_avatar_url=team_avatar_url,
            user_avatar_url=user_avatar_url,
        )

        participant_db_dto.additional_properties = d
        return participant_db_dto

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
