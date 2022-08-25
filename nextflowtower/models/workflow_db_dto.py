import datetime
from typing import Any, Dict, List, Type, TypeVar, cast

import attr
from dateutil.parser import isoparse

from ..models.wf_manifest import WfManifest
from ..models.wf_nextflow import WfNextflow
from ..models.wf_stats import WfStats
from ..models.workflow_db_dto_params import WorkflowDbDtoParams
from ..models.workflow_status import WorkflowStatus

T = TypeVar("T", bound="WorkflowDbDto")


@attr.s(auto_attribs=True)
class WorkflowDbDto:
    """
    Attributes:
        start (datetime.datetime):
        params (WorkflowDbDtoParams):
        profile (str):
        duration (int):
        command_line (str):
        container (str):
        project_dir (str):
        owner_id (int):
        repository (str):
        id (str):
        submit (datetime.datetime):
        complete (datetime.datetime):
        date_created (datetime.datetime):
        last_updated (datetime.datetime):
        run_name (str):
        session_id (str):
        work_dir (str):
        commit_id (str):
        user_name (str):
        script_id (str):
        revision (str):
        project_name (str):
        script_name (str):
        launch_id (str):
        status (WorkflowStatus):
        config_files (List[str]):
        config_text (str):
        manifest (WfManifest):
        nextflow (WfNextflow):
        stats (WfStats):
        error_message (str):
        error_report (str):
        deleted (bool):
        home_dir (str):
        container_engine (str):
        script_file (str):
        launch_dir (str):
        exit_status (int):
        resume (bool):
        success (bool):
    """

    start: datetime.datetime
    params: WorkflowDbDtoParams
    profile: str
    duration: int
    command_line: str
    container: str
    project_dir: str
    owner_id: int
    repository: str
    id: str
    submit: datetime.datetime
    complete: datetime.datetime
    date_created: datetime.datetime
    last_updated: datetime.datetime
    run_name: str
    session_id: str
    work_dir: str
    commit_id: str
    user_name: str
    script_id: str
    revision: str
    project_name: str
    script_name: str
    launch_id: str
    status: WorkflowStatus
    config_files: List[str]
    config_text: str
    manifest: WfManifest
    nextflow: WfNextflow
    stats: WfStats
    error_message: str
    error_report: str
    deleted: bool
    home_dir: str
    container_engine: str
    script_file: str
    launch_dir: str
    exit_status: int
    resume: bool
    success: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        start = self.start.isoformat()

        params = self.params.to_dict()

        profile = self.profile
        duration = self.duration
        command_line = self.command_line
        container = self.container
        project_dir = self.project_dir
        owner_id = self.owner_id
        repository = self.repository
        id = self.id
        submit = self.submit.isoformat()

        complete = self.complete.isoformat()

        date_created = self.date_created.isoformat()

        last_updated = self.last_updated.isoformat()

        run_name = self.run_name
        session_id = self.session_id
        work_dir = self.work_dir
        commit_id = self.commit_id
        user_name = self.user_name
        script_id = self.script_id
        revision = self.revision
        project_name = self.project_name
        script_name = self.script_name
        launch_id = self.launch_id
        status = self.status.value

        config_files = self.config_files

        config_text = self.config_text
        manifest = self.manifest.to_dict()

        nextflow = self.nextflow.to_dict()

        stats = self.stats.to_dict()

        error_message = self.error_message
        error_report = self.error_report
        deleted = self.deleted
        home_dir = self.home_dir
        container_engine = self.container_engine
        script_file = self.script_file
        launch_dir = self.launch_dir
        exit_status = self.exit_status
        resume = self.resume
        success = self.success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start": start,
                "params": params,
                "profile": profile,
                "duration": duration,
                "commandLine": command_line,
                "container": container,
                "projectDir": project_dir,
                "ownerId": owner_id,
                "repository": repository,
                "id": id,
                "submit": submit,
                "complete": complete,
                "dateCreated": date_created,
                "lastUpdated": last_updated,
                "runName": run_name,
                "sessionId": session_id,
                "workDir": work_dir,
                "commitId": commit_id,
                "userName": user_name,
                "scriptId": script_id,
                "revision": revision,
                "projectName": project_name,
                "scriptName": script_name,
                "launchId": launch_id,
                "status": status,
                "configFiles": config_files,
                "configText": config_text,
                "manifest": manifest,
                "nextflow": nextflow,
                "stats": stats,
                "errorMessage": error_message,
                "errorReport": error_report,
                "deleted": deleted,
                "homeDir": home_dir,
                "containerEngine": container_engine,
                "scriptFile": script_file,
                "launchDir": launch_dir,
                "exitStatus": exit_status,
                "resume": resume,
                "success": success,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        start = isoparse(d.pop("start"))

        params = WorkflowDbDtoParams.from_dict(d.pop("params"))

        profile = d.pop("profile")

        duration = d.pop("duration")

        command_line = d.pop("commandLine")

        container = d.pop("container")

        project_dir = d.pop("projectDir")

        owner_id = d.pop("ownerId")

        repository = d.pop("repository")

        id = d.pop("id")

        submit = isoparse(d.pop("submit"))

        complete = isoparse(d.pop("complete"))

        date_created = isoparse(d.pop("dateCreated"))

        last_updated = isoparse(d.pop("lastUpdated"))

        run_name = d.pop("runName")

        session_id = d.pop("sessionId")

        work_dir = d.pop("workDir")

        commit_id = d.pop("commitId")

        user_name = d.pop("userName")

        script_id = d.pop("scriptId")

        revision = d.pop("revision")

        project_name = d.pop("projectName")

        script_name = d.pop("scriptName")

        launch_id = d.pop("launchId")

        status = WorkflowStatus(d.pop("status"))

        config_files = cast(List[str], d.pop("configFiles"))

        config_text = d.pop("configText")

        manifest = WfManifest.from_dict(d.pop("manifest"))

        nextflow = WfNextflow.from_dict(d.pop("nextflow"))

        stats = WfStats.from_dict(d.pop("stats"))

        error_message = d.pop("errorMessage")

        error_report = d.pop("errorReport")

        deleted = d.pop("deleted")

        home_dir = d.pop("homeDir")

        container_engine = d.pop("containerEngine")

        script_file = d.pop("scriptFile")

        launch_dir = d.pop("launchDir")

        exit_status = d.pop("exitStatus")

        resume = d.pop("resume")

        success = d.pop("success")

        workflow_db_dto = cls(
            start=start,
            params=params,
            profile=profile,
            duration=duration,
            command_line=command_line,
            container=container,
            project_dir=project_dir,
            owner_id=owner_id,
            repository=repository,
            id=id,
            submit=submit,
            complete=complete,
            date_created=date_created,
            last_updated=last_updated,
            run_name=run_name,
            session_id=session_id,
            work_dir=work_dir,
            commit_id=commit_id,
            user_name=user_name,
            script_id=script_id,
            revision=revision,
            project_name=project_name,
            script_name=script_name,
            launch_id=launch_id,
            status=status,
            config_files=config_files,
            config_text=config_text,
            manifest=manifest,
            nextflow=nextflow,
            stats=stats,
            error_message=error_message,
            error_report=error_report,
            deleted=deleted,
            home_dir=home_dir,
            container_engine=container_engine,
            script_file=script_file,
            launch_dir=launch_dir,
            exit_status=exit_status,
            resume=resume,
            success=success,
        )

        workflow_db_dto.additional_properties = d
        return workflow_db_dto

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
