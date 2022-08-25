from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.list_dataset_versions_response import ListDatasetVersionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspaceId}/datasets/{datasetId}/versions".format(
        client.base_url, workspaceId=workspace_id, datasetId=dataset_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["mimeType"] = mime_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    if response.status_code == 200:
        response_200 = ListDatasetVersionsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all versions of a dataset

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        mime_type=mime_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all versions of a dataset

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        mime_type=mime_type,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all versions of a dataset

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        client=client,
        mime_type=mime_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: int,
    dataset_id: str,
    *,
    client: AuthenticatedClient,
    mime_type: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]:
    """List all versions of a dataset

    Args:
        workspace_id (int):
        dataset_id (str):
        mime_type (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, ErrorResponse, ListDatasetVersionsResponse]]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            dataset_id=dataset_id,
            client=client,
            mime_type=mime_type,
        )
    ).parsed
