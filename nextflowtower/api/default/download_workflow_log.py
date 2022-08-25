from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    file_name: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/{workflowId}/download".format(client.base_url, workflowId=workflow_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["fileName"] = file_name

    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.json()))

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, File]]:
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
    file_name: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download Workflow files of the Nextflow main job

    Args:
        workflow_id (str):
        file_name (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        file_name=file_name,
        workspace_id=workspace_id,
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
    file_name: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download Workflow files of the Nextflow main job

    Args:
        workflow_id (str):
        file_name (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        file_name=file_name,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    file_name: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download Workflow files of the Nextflow main job

    Args:
        workflow_id (str):
        file_name (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        file_name=file_name,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    file_name: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download Workflow files of the Nextflow main job

    Args:
        workflow_id (str):
        file_name (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            file_name=file_name,
            workspace_id=workspace_id,
        )
    ).parsed
