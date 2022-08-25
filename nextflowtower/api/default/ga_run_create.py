from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.run_id import RunId
from ...models.run_request import RunRequest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Dict[str, Any]:
    url = "{}/ga4gh/wes/v1/runs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_body.to_dict()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, RunId]]:
    if response.status_code == 200:
        response_200 = RunId.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, RunId]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Response[Union[Any, ErrorResponse, RunId]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Optional[Union[Any, ErrorResponse, RunId]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Response[Union[Any, ErrorResponse, RunId]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: RunRequest,
    json_body: RunRequest,
) -> Optional[Union[Any, ErrorResponse, RunId]]:
    """GA4GH create a new run

    Args:
        multipart_data (RunRequest):
        json_body (RunRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
            json_body=json_body,
        )
    ).parsed
