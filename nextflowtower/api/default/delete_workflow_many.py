from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.delete_workflows_request import DeleteWorkflowsRequest
from ...models.delete_workflows_response import DeleteWorkflowsResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: DeleteWorkflowsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/delete".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]:
    if response.status_code == 204:
        response_204 = DeleteWorkflowsResponse.from_dict(response.json())

        return response_204
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DeleteWorkflowsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]:
    """Delete several workflow entities given their ids

    Args:
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):
        json_body (DeleteWorkflowsRequest):

    Returns:
        Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
        force=force,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: DeleteWorkflowsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]:
    """Delete several workflow entities given their ids

    Args:
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):
        json_body (DeleteWorkflowsRequest):

    Returns:
        Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
        force=force,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: DeleteWorkflowsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]:
    """Delete several workflow entities given their ids

    Args:
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):
        json_body (DeleteWorkflowsRequest):

    Returns:
        Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
        force=force,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: DeleteWorkflowsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]:
    """Delete several workflow entities given their ids

    Args:
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):
        json_body (DeleteWorkflowsRequest):

    Returns:
        Response[Union[Any, DeleteWorkflowsResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
            force=force,
        )
    ).parsed
