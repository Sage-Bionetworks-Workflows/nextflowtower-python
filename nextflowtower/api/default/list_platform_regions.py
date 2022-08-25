from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.list_regions_response import ListRegionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/platforms/{platformId}/regions".format(client.base_url, platformId=platform_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ListRegionsResponse]]:
    if response.status_code == 200:
        response_200 = ListRegionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ListRegionsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListRegionsResponse]]:
    """List available regions for the platform specified

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListRegionsResponse]]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListRegionsResponse]]:
    """List available regions for the platform specified

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListRegionsResponse]]
    """

    return sync_detailed(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListRegionsResponse]]:
    """List available regions for the platform specified

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListRegionsResponse]]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListRegionsResponse]]:
    """List available regions for the platform specified

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, ErrorResponse, ListRegionsResponse]]
    """

    return (
        await asyncio_detailed(
            platform_id=platform_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
