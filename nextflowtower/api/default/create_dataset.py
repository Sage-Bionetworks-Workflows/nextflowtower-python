from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.create_dataset_request import CreateDatasetRequest
from ...models.create_dataset_response import CreateDatasetResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspaceId}/datasets".format(client.base_url, workspaceId=workspace_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateDatasetResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Response[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateDatasetRequest,
) -> Optional[Union[Any, CreateDatasetResponse, ErrorResponse]]:
    """Create a dataset

    Args:
        workspace_id (int):
        json_body (CreateDatasetRequest):

    Returns:
        Response[Union[Any, CreateDatasetResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
