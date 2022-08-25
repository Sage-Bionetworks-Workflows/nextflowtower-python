from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aws_batch_platform_metainfo import AwsBatchPlatformMetainfo
from ..models.google_life_sciences_platform_metainfo import GoogleLifeSciencesPlatformMetainfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="DescribePlatformResponse")


@attr.s(auto_attribs=True)
class DescribePlatformResponse:
    """
    Attributes:
        metainfo (Union[AwsBatchPlatformMetainfo, GoogleLifeSciencesPlatformMetainfo, Unset]):
    """

    metainfo: Union[AwsBatchPlatformMetainfo, GoogleLifeSciencesPlatformMetainfo, Unset] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metainfo: Union[Dict[str, Any], Unset]
        if isinstance(self.metainfo, Unset):
            metainfo = UNSET

        elif isinstance(self.metainfo, AwsBatchPlatformMetainfo):
            metainfo = self.metainfo.to_dict()

        else:
            metainfo = self.metainfo.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if metainfo is not UNSET:
            field_dict["metainfo"] = metainfo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_metainfo(data: object) -> Union[AwsBatchPlatformMetainfo, GoogleLifeSciencesPlatformMetainfo, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_platform_metainfo_type_0 = AwsBatchPlatformMetainfo.from_dict(data)

                return componentsschemas_platform_metainfo_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_platform_metainfo_type_1 = GoogleLifeSciencesPlatformMetainfo.from_dict(data)

            return componentsschemas_platform_metainfo_type_1

        metainfo = _parse_metainfo(d.pop("metainfo", UNSET))

        describe_platform_response = cls(
            metainfo=metainfo,
        )

        describe_platform_response.additional_properties = d
        return describe_platform_response

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
