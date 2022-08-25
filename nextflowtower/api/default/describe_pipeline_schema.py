from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.error_response import ErrorResponse
from ...models.pipeline_schema_attributes import PipelineSchemaAttributes
from ...models.pipeline_schema_response import PipelineSchemaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[PipelineSchemaAttributes]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/pipelines/{pipelineId}/schema".format(client.base_url, pipelineId=pipeline_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["workspaceId"] = workspace_id

    json_attributes: Union[Unset, None, List[str]] = UNSET
    if not isinstance(attributes, Unset):
        if attributes is None:
            json_attributes = None
        else:
            json_attributes = []
            for attributes_item_data in attributes:
                attributes_item = attributes_item_data.value

                json_attributes.append(attributes_item)

    params["attributes"] = json_attributes

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ErrorResponse, PipelineSchemaResponse]]:
    if response.status_code == 200:
        response_200 = PipelineSchemaResponse.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[PipelineSchemaAttributes]] = UNSET,
) -> Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]:
    """Retrieve the Pipeline input schema

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[PipelineSchemaAttributes]]):

    Returns:
        Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[PipelineSchemaAttributes]] = UNSET,
) -> Optional[Union[Any, ErrorResponse, PipelineSchemaResponse]]:
    """Retrieve the Pipeline input schema

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[PipelineSchemaAttributes]]):

    Returns:
        Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]
    """

    return sync_detailed(
        pipeline_id=pipeline_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    ).parsed


async def asyncio_detailed(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[PipelineSchemaAttributes]] = UNSET,
) -> Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]:
    """Retrieve the Pipeline input schema

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[PipelineSchemaAttributes]]):

    Returns:
        Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[PipelineSchemaAttributes]] = UNSET,
) -> Optional[Union[Any, ErrorResponse, PipelineSchemaResponse]]:
    """Retrieve the Pipeline input schema

    Args:
        pipeline_id (int):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[PipelineSchemaAttributes]]):

    Returns:
        Response[Union[Any, ErrorResponse, PipelineSchemaResponse]]
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            workspace_id=workspace_id,
            attributes=attributes,
        )
    ).parsed
