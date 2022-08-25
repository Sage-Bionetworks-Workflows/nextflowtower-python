from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/{workflowId}".format(client.base_url, workflowId=workflow_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["force"] = force

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
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
    force: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Delete the Workflow entity with the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        force=force,
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
    force: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Delete the Workflow entity with the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        force=force,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Delete the Workflow entity with the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        force=force,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    force: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Delete the Workflow entity with the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        force (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            workspace_id=workspace_id,
            force=force,
        )
    ).parsed
