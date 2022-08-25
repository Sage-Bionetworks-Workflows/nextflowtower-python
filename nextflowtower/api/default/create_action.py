from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.create_action_request import CreateActionRequest
from ...models.create_action_response import CreateActionResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CreateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/actions".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CreateActionResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CreateActionResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreateActionResponse, ErrorResponse]]:
    """Create a new Pipeline Action

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateActionRequest):

    Returns:
        Response[Union[Any, CreateActionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: CreateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreateActionResponse, ErrorResponse]]:
    """Create a new Pipeline Action

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateActionRequest):

    Returns:
        Response[Union[Any, CreateActionResponse, ErrorResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CreateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, CreateActionResponse, ErrorResponse]]:
    """Create a new Pipeline Action

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateActionRequest):

    Returns:
        Response[Union[Any, CreateActionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: CreateActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, CreateActionResponse, ErrorResponse]]:
    """Create a new Pipeline Action

    Args:
        workspace_id (Union[Unset, None, int]):
        json_body (CreateActionRequest):

    Returns:
        Response[Union[Any, CreateActionResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
