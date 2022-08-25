from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dataset_version_db_dto import DatasetVersionDbDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadDatasetVersionResponse")


@attr.s(auto_attribs=True)
class UploadDatasetVersionResponse:
    """
    Attributes:
        version (Union[Unset, DatasetVersionDbDto]):
    """

    version: Union[Unset, DatasetVersionDbDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.version, Unset):
            version = self.version.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _version = d.pop("version", UNSET)
        version: Union[Unset, DatasetVersionDbDto]
        if isinstance(_version, Unset):
            version = UNSET
        else:
            version = DatasetVersionDbDto.from_dict(_version)

        upload_dataset_version_response = cls(
            version=version,
        )

        upload_dataset_version_response.additional_properties = d
        return upload_dataset_version_response

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
