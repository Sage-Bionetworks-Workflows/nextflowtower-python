from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.describe_pipeline_response import DescribePipelineResponse
from ...models.error_response import ErrorResponse
from ...models.pipeline_query_attribute import PipelineQueryAttribute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/pipelines/{pipelineId}".format(client.base_url, pipelineId=pipeline_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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

    params["workspaceId"] = workspace_id

    params["sourceWorkspaceId"] = source_workspace_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DescribePipelineResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DescribePipelineResponse, ErrorResponse]]:
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
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe a Pipeline

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribePipelineResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        client=client,
        attributes=attributes,
        workspace_id=workspace_id,
        source_workspace_id=source_workspace_id,
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
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe a Pipeline

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribePipelineResponse, ErrorResponse]]
    """

    return sync_detailed(
        pipeline_id=pipeline_id,
        client=client,
        attributes=attributes,
        workspace_id=workspace_id,
        source_workspace_id=source_workspace_id,
    ).parsed


async def asyncio_detailed(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe a Pipeline

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribePipelineResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        pipeline_id=pipeline_id,
        client=client,
        attributes=attributes,
        workspace_id=workspace_id,
        source_workspace_id=source_workspace_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    pipeline_id: int,
    *,
    client: AuthenticatedClient,
    attributes: Union[Unset, None, List[PipelineQueryAttribute]] = UNSET,
    workspace_id: Union[Unset, None, int] = UNSET,
    source_workspace_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, DescribePipelineResponse, ErrorResponse]]:
    """Describe a Pipeline

    Args:
        pipeline_id (int):
        attributes (Union[Unset, None, List[PipelineQueryAttribute]]):
        workspace_id (Union[Unset, None, int]):
        source_workspace_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, DescribePipelineResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            pipeline_id=pipeline_id,
            client=client,
            attributes=attributes,
            workspace_id=workspace_id,
            source_workspace_id=source_workspace_id,
        )
    ).parsed
