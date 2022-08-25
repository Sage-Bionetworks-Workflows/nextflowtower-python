from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.action_query_attribute import ActionQueryAttribute
from ...models.describe_action_response import DescribeActionResponse
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    action_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ActionQueryAttribute]] = UNSET,
) -> Dict[str, Any]:
    url = "{}/actions/{actionId}".format(client.base_url, actionId=action_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DescribeActionResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DescribeActionResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DescribeActionResponse, ErrorResponse]]:
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
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ActionQueryAttribute]] = UNSET,
) -> Response[Union[Any, DescribeActionResponse, ErrorResponse]]:
    """Describe an existing Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ActionQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeActionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
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
    action_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ActionQueryAttribute]] = UNSET,
) -> Optional[Union[Any, DescribeActionResponse, ErrorResponse]]:
    """Describe an existing Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ActionQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeActionResponse, ErrorResponse]]
    """

    return sync_detailed(
        action_id=action_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    ).parsed


async def asyncio_detailed(
    action_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ActionQueryAttribute]] = UNSET,
) -> Response[Union[Any, DescribeActionResponse, ErrorResponse]]:
    """Describe an existing Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ActionQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeActionResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        action_id=action_id,
        client=client,
        workspace_id=workspace_id,
        attributes=attributes,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    action_id: str,
    *,
    client: AuthenticatedClient,
    workspace_id: Union[Unset, None, int] = UNSET,
    attributes: Union[Unset, None, List[ActionQueryAttribute]] = UNSET,
) -> Optional[Union[Any, DescribeActionResponse, ErrorResponse]]:
    """Describe an existing Pipeline Action

    Args:
        action_id (str):
        workspace_id (Union[Unset, None, int]):
        attributes (Union[Unset, None, List[ActionQueryAttribute]]):

    Returns:
        Response[Union[Any, DescribeActionResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            action_id=action_id,
            client=client,
            workspace_id=workspace_id,
            attributes=attributes,
        )
    ).parsed
