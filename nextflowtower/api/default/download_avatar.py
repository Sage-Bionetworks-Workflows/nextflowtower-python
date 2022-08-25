from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/avatars/{avatarId}".format(client.base_url, avatarId=avatar_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.json()))

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, File]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        avatar_id=avatar_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    return sync_detailed(
        avatar_id=avatar_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        avatar_id=avatar_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    avatar_id: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the avatar image

    Args:
        avatar_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    return (
        await asyncio_detailed(
            avatar_id=avatar_id,
            client=client,
        )
    ).parsed
