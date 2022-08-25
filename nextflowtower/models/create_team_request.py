from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.team import Team
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTeamRequest")


@attr.s(auto_attribs=True)
class CreateTeamRequest:
    """
    Attributes:
        team (Union[Unset, Team]):
        avatar_id (Union[Unset, str]):
    """

    team: Union[Unset, Team] = UNSET
    avatar_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        avatar_id = self.avatar_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _team = d.pop("team", UNSET)
        team: Union[Unset, Team]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = Team.from_dict(_team)

        avatar_id = d.pop("avatarId", UNSET)

        create_team_request = cls(
            team=team,
            avatar_id=avatar_id,
        )

        create_team_request.additional_properties = d
        return create_team_request

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
