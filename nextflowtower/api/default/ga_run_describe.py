from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.run_log import RunLog
from ...types import Response


def _get_kwargs(
    run_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ga4gh/wes/v1/runs/{run_id}".format(client.base_url, run_id=run_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, RunLog]]:
    if response.status_code == 200:
        response_200 = RunLog.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, RunLog]]:
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
) -> Response[Union[Any, ErrorResponse, RunLog]]:
    """GA4GH describe run

    Args:
        run_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, RunLog]]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        client=client,
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
) -> Optional[Union[Any, ErrorResponse, RunLog]]:
    """GA4GH describe run

    Args:
        run_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, RunLog]]
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse, RunLog]]:
    """GA4GH describe run

    Args:
        run_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, RunLog]]
    """

    kwargs = _get_kwargs(
        run_id=run_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    run_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ErrorResponse, RunLog]]:
    """GA4GH describe run

    Args:
        run_id (str):

    Returns:
        Response[Union[Any, ErrorResponse, RunLog]]
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
        )
    ).parsed
