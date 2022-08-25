from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.describe_workflow_response import DescribeWorkflowResponse
from ...models.error_response import ErrorResponse
from ...models.workflow_query_attribute import WorkflowQueryAttribute
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[WorkflowQueryAttribute]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/workflow/{workflowId}".format(client.base_url, workflowId=workflow_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DescribeWorkflowResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DescribeWorkflowResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[WorkflowQueryAttribute]] = UNSET,
) -> Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]:
    """Describe the Workflow entity for the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[WorkflowQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
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
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[WorkflowQueryAttribute]] = UNSET,
) -> Optional[Union[Any, DescribeWorkflowResponse, ErrorResponse]]:
    """Describe the Workflow entity for the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[WorkflowQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]
    """

    return sync_detailed(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    ).parsed


async def asyncio_detailed(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[WorkflowQueryAttribute]] = UNSET,
) -> Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]:
    """Describe the Workflow entity for the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[WorkflowQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        workflow_id=workflow_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    workflow_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[WorkflowQueryAttribute]] = UNSET,
) -> Optional[Union[Any, DescribeWorkflowResponse, ErrorResponse]]:
    """Describe the Workflow entity for the given ID

    Args:
        workflow_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[WorkflowQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeWorkflowResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            workflow_id=workflow_id,
            client=client,
            workspace_id=workspace_id,
            attributes=attributes,
        )
    ).parsed
