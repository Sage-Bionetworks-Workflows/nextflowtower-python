from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.list_members_response import ListMembersResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    org_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/orgs/{orgId}/members".format(client.base_url, orgId=org_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["max"] = max_

    params["offset"] = offset

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ListMembersResponse]]:
    if response.status_code == 200:
        response_200 = ListMembersResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ListMembersResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListMembersResponse]]:
    """List all members of an organization

    Args:
        org_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListMembersResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        max_=max_,
        offset=offset,
        search=search,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    org_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListMembersResponse]]:
    """List all members of an organization

    Args:
        org_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListMembersResponse]]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        max_=max_,
        offset=offset,
        search=search,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListMembersResponse]]:
    """List all members of an organization

    Args:
        org_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListMembersResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        max_=max_,
        offset=offset,
        search=search,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org_id: int,
    *,
    client: AuthenticatedClient,
    max_: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListMembersResponse]]:
    """List all members of an organization

    Args:
        org_id (int):
        max_ (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        search (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListMembersResponse]]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            max_=max_,
            offset=offset,
            search=search,
        )
    ).parsed
