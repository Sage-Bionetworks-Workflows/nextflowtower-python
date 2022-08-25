from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.list_compute_envs_response import ListComputeEnvsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/compute-envs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["status"] = status

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ListComputeEnvsResponse]]:
    if response.status_code == 200:
        response_200 = ListComputeEnvsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]:
    """List all Tower compute environments for the authenticated user or given workspace

    Args:
        status (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
        workspace_id=workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListComputeEnvsResponse]]:
    """List all Tower compute environments for the authenticated user or given workspace

    Args:
        status (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]
    """

    return sync_detailed(
        client=client,
        status=status,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]:
    """List all Tower compute environments for the authenticated user or given workspace

    Args:
        status (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        status=status,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: Union[Unset, None, str] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListComputeEnvsResponse]]:
    """List all Tower compute environments for the authenticated user or given workspace

    Args:
        status (Union[Unset, None, str]):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListComputeEnvsResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            workspace_id=workspace_id,
        )
    ).parsed
