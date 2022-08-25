from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.list_workspaces_and_org_response import ListWorkspacesAndOrgResponse
from ...types import Response


def _get_kwargs(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/user/{userId}/workspaces".format(client.base_url, userId=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]:
    if response.status_code == 200:
        response_200 = ListWorkspacesAndOrgResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]:
    """List the workspaces and organizations of a given user

    Args:
        user_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]:
    """List the workspaces and organizations of a given user

    Args:
        user_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]:
    """List the workspaces and organizations of a given user

    Args:
        user_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]:
    """List the workspaces and organizations of a given user

    Args:
        user_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesAndOrgResponse]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
        )
    ).parsed
