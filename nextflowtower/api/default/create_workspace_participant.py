from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.add_participant_request import AddParticipantRequest
from ...models.add_participant_response import AddParticipantResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddParticipantRequest,
) -> Dict[str, Any]:
    url = "{}/orgs/{orgId}/workspaces/{workspaceId}/participants/add".format(
        client.base_url, orgId=org_id, workspaceId=workspace_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[AddParticipantResponse, Any, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddParticipantResponse.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[AddParticipantResponse, Any, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddParticipantRequest,
) -> Response[Union[AddParticipantResponse, Any, ErrorResponse]]:
    """Create a new workspace participant

    Args:
        org_id (int):
        workspace_id (int):
        json_body (AddParticipantRequest):

    Returns:
        Response[Union[AddParticipantResponse, Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
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
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddParticipantRequest,
) -> Optional[Union[AddParticipantResponse, Any, ErrorResponse]]:
    """Create a new workspace participant

    Args:
        org_id (int):
        workspace_id (int):
        json_body (AddParticipantRequest):

    Returns:
        Response[Union[AddParticipantResponse, Any, ErrorResponse]]
    """

    return sync_detailed(
        org_id=org_id,
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddParticipantRequest,
) -> Response[Union[AddParticipantResponse, Any, ErrorResponse]]:
    """Create a new workspace participant

    Args:
        org_id (int):
        workspace_id (int):
        json_body (AddParticipantRequest):

    Returns:
        Response[Union[AddParticipantResponse, Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        workspace_id=workspace_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org_id: int,
    workspace_id: int,
    *,
    client: AuthenticatedClient,
    json_body: AddParticipantRequest,
) -> Optional[Union[AddParticipantResponse, Any, ErrorResponse]]:
    """Create a new workspace participant

    Args:
        org_id (int):
        workspace_id (int):
        json_body (AddParticipantRequest):

    Returns:
        Response[Union[AddParticipantResponse, Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            workspace_id=workspace_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
