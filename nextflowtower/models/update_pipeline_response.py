from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.pipeline_db_dto import PipelineDbDto
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdatePipelineResponse")


@attr.s(auto_attribs=True)
class UpdatePipelineResponse:
    """
    Attributes:
        pipeline (Union[Unset, PipelineDbDto]):
    """

    pipeline: Union[Unset, PipelineDbDto] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pipeline: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline, Unset):
            pipeline = self.pipeline.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline is not UNSET:
            field_dict["pipeline"] = pipeline

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pipeline = d.pop("pipeline", UNSET)
        pipeline: Union[Unset, PipelineDbDto]
        if isinstance(_pipeline, Unset):
            pipeline = UNSET
        else:
            pipeline = PipelineDbDto.from_dict(_pipeline)

        update_pipeline_response = cls(
            pipeline=pipeline,
        )

        update_pipeline_response.additional_properties = d
        return update_pipeline_response

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
