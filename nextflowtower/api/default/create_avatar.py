from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.create_avatar_multipart_data import CreateAvatarMultipartData
from ...models.create_avatar_response import CreateAvatarResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAvatarMultipartData,
) -> Dict[str, Any]:
    url = "{}/avatars".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CreateAvatarResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateAvatarResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CreateAvatarResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAvatarMultipartData,
) -> Response[Union[Any, CreateAvatarResponse, ErrorResponse]]:
    """Create the avatar image

    Args:
        multipart_data (CreateAvatarMultipartData):

    Returns:
        Response[Union[Any, CreateAvatarResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAvatarMultipartData,
) -> Optional[Union[Any, CreateAvatarResponse, ErrorResponse]]:
    """Create the avatar image

    Args:
        multipart_data (CreateAvatarMultipartData):

    Returns:
        Response[Union[Any, CreateAvatarResponse, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAvatarMultipartData,
) -> Response[Union[Any, CreateAvatarResponse, ErrorResponse]]:
    """Create the avatar image

    Args:
        multipart_data (CreateAvatarMultipartData):

    Returns:
        Response[Union[Any, CreateAvatarResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    multipart_data: CreateAvatarMultipartData,
) -> Optional[Union[Any, CreateAvatarResponse, ErrorResponse]]:
    """Create the avatar image

    Args:
        multipart_data (CreateAvatarMultipartData):

    Returns:
        Response[Union[Any, CreateAvatarResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
