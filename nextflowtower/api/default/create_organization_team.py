from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.create_team_request import CreateTeamRequest
from ...models.create_team_response import CreateTeamResponse
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateTeamRequest,
) -> Dict[str, Any]:
    url = "{}/orgs/{orgId}/teams".format(client.base_url, orgId=org_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CreateTeamResponse, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateTeamResponse.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CreateTeamResponse, ErrorResponse]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateTeamRequest,
) -> Response[Union[Any, CreateTeamResponse, ErrorResponse]]:
    """Create a new organization team

    Args:
        org_id (int):
        json_body (CreateTeamRequest):

    Returns:
        Response[Union[Any, CreateTeamResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
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
    *,
    client: AuthenticatedClient,
    json_body: CreateTeamRequest,
) -> Optional[Union[Any, CreateTeamResponse, ErrorResponse]]:
    """Create a new organization team

    Args:
        org_id (int):
        json_body (CreateTeamRequest):

    Returns:
        Response[Union[Any, CreateTeamResponse, ErrorResponse]]
    """

    return sync_detailed(
        org_id=org_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateTeamRequest,
) -> Response[Union[Any, CreateTeamResponse, ErrorResponse]]:
    """Create a new organization team

    Args:
        org_id (int):
        json_body (CreateTeamRequest):

    Returns:
        Response[Union[Any, CreateTeamResponse, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        org_id=org_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    org_id: int,
    *,
    client: AuthenticatedClient,
    json_body: CreateTeamRequest,
) -> Optional[Union[Any, CreateTeamResponse, ErrorResponse]]:
    """Create a new organization team

    Args:
        org_id (int):
        json_body (CreateTeamRequest):

    Returns:
        Response[Union[Any, CreateTeamResponse, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            org_id=org_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
