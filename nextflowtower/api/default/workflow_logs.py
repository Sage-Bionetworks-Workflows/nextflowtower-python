from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.workflow_log_response import WorkflowLogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    next_: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/{workflowId}/log".format(client.base_url, workflowId=workflow_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["next"] = next_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    if response.status_code == 200:
        response_200 = WorkflowLogResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    next_: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Retrieve Workflow output logs of the Nextflow main job

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        next_ (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, WorkflowLogResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        next_=next_,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    next_: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Retrieve Workflow output logs of the Nextflow main job

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        next_ (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, WorkflowLogResponse]]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        next_=next_,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    next_: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Retrieve Workflow output logs of the Nextflow main job

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        next_ (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, WorkflowLogResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        next_=next_,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    next_: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, WorkflowLogResponse]]:
    """Retrieve Workflow output logs of the Nextflow main job

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        next_ (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, WorkflowLogResponse]]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            workspace_id=workspace_id,
            next_=next_,
        )
    ).parsed
