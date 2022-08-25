from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_workflow_star_response import CreateWorkflowStarResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    client: Client,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/{workflowId}/star".format(client.base_url, workflowId=workflow_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateWorkflowStarResponse.from_dict(response.json())

        return response_200
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: Client,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]:
    """Star a workflow

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
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
    client: Client,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]:
    """Star a workflow

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: Client,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]:
    """Star a workflow

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: Client,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]:
    """Star a workflow

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, CreateWorkflowStarResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
