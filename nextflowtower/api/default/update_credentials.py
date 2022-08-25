from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.update_credentials_request import UpdateCredentialsRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateCredentialsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/credentials/{credentialsId}".format(client.base_url, credentialsId=credentials_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateCredentialsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Update the credentials data for the given id

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateCredentialsRequest):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        credentials_id=credentials_id,
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
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateCredentialsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update the credentials data for the given id

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateCredentialsRequest):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        credentials_id=credentials_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    ).parsed


async def asyncio_detailed(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateCredentialsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ErrorResponse]]:
    """Update the credentials data for the given id

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateCredentialsRequest):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        credentials_id=credentials_id,
        client=client,
        json_body=json_body,
        workspace_id=workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    credentials_id: str,
    *,
    client: AuthenticatedClient,
    json_body: UpdateCredentialsRequest,
    workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ErrorResponse]]:
    """Update the credentials data for the given id

    Args:
        credentials_id (str):
        workspace_id (Union[Unset, None, int]):
        json_body (UpdateCredentialsRequest):

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            credentials_id=credentials_id,
            client=client,
            json_body=json_body,
            workspace_id=workspace_id,
        )
    ).parsed
