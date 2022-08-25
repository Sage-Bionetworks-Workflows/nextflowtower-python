from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.team_db_dto import TeamDbDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTeamResponse")


@attr.s(auto_attribs=True)
class CreateTeamResponse:
    """
    Attributes:
        team (Union[Unset, TeamDbDto]):
    """

    team: Union[Unset, TeamDbDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.team, Unset):
            team = self.team.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team is not UNSET:
            field_dict["team"] = team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _team = d.pop("team", UNSET)
        team: Union[Unset, TeamDbDto]
        if isinstance(_team, Unset):
            team = UNSET
        else:
            team = TeamDbDto.from_dict(_team)

        create_team_response = cls(
            team=team,
        )

        create_team_response.additional_properties = d
        return create_team_response

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
