from io import BytesIO
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...types import File, Response


def _get_kwargs(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/workspaces/{workspaceId}/datasets/{datasetId}/v/{version}/n/{fileName}".format(
        client.base_url, workspaceId=workspace_id, datasetId=dataset_id, version=version, fileName=file_name
    )

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
        response_404 = ErrorResponse.from_dict(response.json())

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
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        version=version,
        file_name=file_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    return sync_detailed(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        version=version,
        file_name=file_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    kwargs = _get_kwargs(
        workspace_id=workspace_id,
        dataset_id=dataset_id,
        version=version,
        file_name=file_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workspace_id: int,
    dataset_id: str,
    version: str,
    file_name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, ErrorResponse, File]]:
    """Download the content of a dataset version

    Args:
        workspace_id (int):
        dataset_id (str):
        version (str):
        file_name (str):

    Returns:
        Response[Union[Any, ErrorResponse, File]]
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            dataset_id=dataset_id,
            version=version,
            file_name=file_name,
            client=client,
        )
    ).parsed
