from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.task import Task
from ..models.trace_progress_data import TraceProgressData
from ..types import UNSET, Unset

T = TypeVar("T", bound="TraceProgressRequest")


@attr.s(auto_attribs=True)
class TraceProgressRequest:
    """
    Attributes:
        tasks (Union[Unset, List[Task]]):
        progress (Union[Unset, TraceProgressData]):
    """

    tasks: Union[Unset, List[Task]] = UNSET
    progress: Union[Unset, TraceProgressData] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        progress: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.progress, Unset):
            progress = self.progress.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if progress is not UNSET:
            field_dict["progress"] = progress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = Task.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        _progress = d.pop("progress", UNSET)
        progress: Union[Unset, TraceProgressData]
        if isinstance(_progress, Unset):
            progress = UNSET
        else:
            progress = TraceProgressData.from_dict(_progress)

        trace_progress_request = cls(
            tasks=tasks,
            progress=progress,
        )

        trace_progress_request.additional_properties = d
        return trace_progress_request

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
