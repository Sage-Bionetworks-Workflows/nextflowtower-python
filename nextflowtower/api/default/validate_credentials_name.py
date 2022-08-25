from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credentials/validate".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
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
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Check that is a valid credentials name

    Args:
        workspace_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        workspace_id=workspace_id,
        name=name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Check that is a valid credentials name

    Args:
        workspace_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        workspace_id=workspace_id,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Check that is a valid credentials name

    Args:
        workspace_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        workspace_id=workspace_id,
        name=name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    name: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Check that is a valid credentials name

    Args:
        workspace_id (Union[Unset, None, int]):
        name (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            workspace_id=workspace_id,
            name=name,
        )
    ).parsed
