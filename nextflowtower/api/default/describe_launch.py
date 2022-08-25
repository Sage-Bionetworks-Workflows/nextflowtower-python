from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.describe_launch_response import DescribeLaunchResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    launch_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/launch/{launchId}".format(client.base_url, launchId=launch_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DescribeLaunchResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DescribeLaunchResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    launch_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]:
    """Describe the Launch record for the given id

    Args:
        launch_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        launch_id=launch_id,
        client=client,
        workspace_id=workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    launch_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribeLaunchResponse, ErrorResponse]]:
    """Describe the Launch record for the given id

    Args:
        launch_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]
    """

    return sync_detailed(
        launch_id=launch_id,
        client=client,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    launch_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]:
    """Describe the Launch record for the given id

    Args:
        launch_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        launch_id=launch_id,
        client=client,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    launch_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribeLaunchResponse, ErrorResponse]]:
    """Describe the Launch record for the given id

    Args:
        launch_id (str):
        workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribeLaunchResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            launch_id=launch_id,
            client=client,
            workspace_id=workspace_id,
        )
    ).parsed
