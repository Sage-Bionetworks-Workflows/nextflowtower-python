from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.empty_body_request import EmptyBodyRequest
from ...models.error_response import ErrorResponse
from ...models.run_id import RunId
from ...types import Response


def _get_kwargs(
    run_id: str,
    *,
    client: Client,
    json_body: EmptyBodyRequest,
) -> Dict[str, Any]:
    url = "{}/ga4gh/wes/v1/runs/{run_id}/cancel".format(client.base_url, run_id=run_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    run_id: str,
    *,
    client: Client,
    json_body: EmptyBodyRequest,
) -> Response[Union[Any, ErrorResponse, RunId]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    run_id: str,
    *,
    client: Client,
    json_body: EmptyBodyRequest,
) -> Optional[Union[Any, ErrorResponse, RunId]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: Client,
    json_body: EmptyBodyRequest,
) -> Response[Union[Any, ErrorResponse, RunId]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    run_id: str,
    *,
    client: Client,
    json_body: EmptyBodyRequest,
) -> Optional[Union[Any, ErrorResponse, RunId]]:
    """GA4GH cancel a run

    Args:
        run_id (str):
        json_body (EmptyBodyRequest):

    Returns:
        Response[Union[Any, ErrorResponse, RunId]]
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
