from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.launch_action_request import LaunchActionRequest
from ...models.launch_action_response import LaunchActionResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/actions/{actionId}/launch".format(client.base_url, actionId=action_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, LaunchActionResponse]]:
    if response.status_code == 200:
        response_200 = LaunchActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, LaunchActionResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger the execution of a Tower Launch Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Returns:
        Response[Union[Any, ErrorResponse, LaunchActionResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
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
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger the execution of a Tower Launch Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Returns:
        Response[Union[Any, ErrorResponse, LaunchActionResponse]]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger the execution of a Tower Launch Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Returns:
        Response[Union[Any, ErrorResponse, LaunchActionResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    action_id: str,
    *,
    client: AuthenticatedClient,
    json_body: LaunchActionRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse, LaunchActionResponse]]:
    """Trigger the execution of a Tower Launch Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (LaunchActionRequest):

    Returns:
        Response[Union[Any, ErrorResponse, LaunchActionResponse]]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
