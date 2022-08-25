from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user import User
from ..types import UNSET, Unset

T = TypeVar("T", bound="DescribeUserResponse")


@attr.s(auto_attribs=True)
class DescribeUserResponse:
    """
    Attributes:
        user (Union[Unset, User]):
        need_consent (Union[Unset, bool]):
        default_workspace_id (Union[Unset, int]):
    """

    user: Union[Unset, User] = UNSET
    need_consent: Union[Unset, bool] = UNSET
    default_workspace_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        need_consent = self.need_consent
        default_workspace_id = self.default_workspace_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user is not UNSET:
            field_dict["user"] = user
        if need_consent is not UNSET:
            field_dict["needConsent"] = need_consent
        if default_workspace_id is not UNSET:
            field_dict["defaultWorkspaceId"] = default_workspace_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _user = d.pop("user", UNSET)
        user: Union[Unset, User]
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        need_consent = d.pop("needConsent", UNSET)

        default_workspace_id = d.pop("defaultWorkspaceId", UNSET)

        describe_user_response = cls(
            user=user,
            need_consent=need_consent,
            default_workspace_id=default_workspace_id,
        )

        describe_user_response.additional_properties = d
        return describe_user_response

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
