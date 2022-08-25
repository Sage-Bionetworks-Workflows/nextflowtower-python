from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.describe_platform_response import DescribePlatformResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Dict[str, Any]:
    url = "{}/platforms/{platformId}".format(client.base_url, platformId=platform_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["regionId"] = region_id

    params["credentialsId"] = credentials_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DescribePlatformResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DescribePlatformResponse, ErrorResponse]]:
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
    region_id: str,
    credentials_id: str,
) -> Response[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe the platform entity for the given id

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Returns:
        Response[Union[Any, DescribePlatformResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
        region_id=region_id,
        credentials_id=credentials_id,
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
    region_id: str,
    credentials_id: str,
) -> Optional[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe the platform entity for the given id

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Returns:
        Response[Union[Any, DescribePlatformResponse, ErrorResponse]]
    """

    return sync_detailed(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
        region_id=region_id,
        credentials_id=credentials_id,
    ).parsed


async def asyncio_detailed(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Response[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe the platform entity for the given id

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Returns:
        Response[Union[Any, DescribePlatformResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        platform_id=platform_id,
        client=client,
        workspace_id=workspace_id,
        region_id=region_id,
        credentials_id=credentials_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    platform_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    region_id: str,
    credentials_id: str,
) -> Optional[Union[Any, DescribePlatformResponse, ErrorResponse]]:
    """Describe the platform entity for the given id

    Args:
        platform_id (str):
        workspace_id (Union[Unset, None, int]):
        region_id (str):
        credentials_id (str):

    Returns:
        Response[Union[Any, DescribePlatformResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            platform_id=platform_id,
            client=client,
            workspace_id=workspace_id,
            region_id=region_id,
            credentials_id=credentials_id,
        )
    ).parsed
