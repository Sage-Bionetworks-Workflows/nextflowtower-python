from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.list_workspaces_response import ListWorkspacesResponse
from ...types import Response


def _get_kwargs(
    org_id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/orgs/{orgId}/workspaces".format(client.base_url, orgId=org_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ListWorkspacesResponse]]:
    if response.status_code == 200:
        response_200 = ListWorkspacesResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]:
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
) -> Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]:
    """List the workspaces of a given organization accessible by the authenticated user

    Args:
        org_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
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
) -> Optional[Union[Any, ErrorResponse, ListWorkspacesResponse]]:
    """List the workspaces of a given organization accessible by the authenticated user

    Args:
        org_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]:
    """List the workspaces of a given organization accessible by the authenticated user

    Args:
        org_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, ListWorkspacesResponse]]:
    """List the workspaces of a given organization accessible by the authenticated user

    Args:
        org_id (int):

    Returns:
        Response[Union[Any, ErrorResponse, ListWorkspacesResponse]]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
        )
    ).parsed
