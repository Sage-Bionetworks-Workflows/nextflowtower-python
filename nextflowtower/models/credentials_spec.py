import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.agent_security_keys import AgentSecurityKeys
from ..models.aws_security_keys import AwsSecurityKeys
from ..models.azure_security_keys import AzureSecurityKeys
from ..models.bit_bucket_security_keys import BitBucketSecurityKeys
from ..models.code_commit_security_keys import CodeCommitSecurityKeys
from ..models.container_registry_keys import ContainerRegistryKeys
from ..models.credentials_spec_provider import CredentialsSpecProvider
from ..models.git_hub_security_keys import GitHubSecurityKeys
from ..models.git_lab_security_keys import GitLabSecurityKeys
from ..models.google_security_keys import GoogleSecurityKeys
from ..models.k8s_security_keys import K8SSecurityKeys
from ..models.ssh_security_keys import SSHSecurityKeys
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialsSpec")


@attr.s(auto_attribs=True)
class CredentialsSpec:
    """
    Attributes:
        name (str):
        keys (Union[AgentSecurityKeys, AwsSecurityKeys, AzureSecurityKeys, BitBucketSecurityKeys,
            CodeCommitSecurityKeys, ContainerRegistryKeys, GitHubSecurityKeys, GitLabSecurityKeys, GoogleSecurityKeys,
            K8SSecurityKeys, SSHSecurityKeys, Unset]):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        provider (Union[Unset, CredentialsSpecProvider]):
        base_url (Union[Unset, str]):
        category (Union[Unset, str]):
        deleted (Union[Unset, bool]):
        last_used (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, datetime.datetime]):
        last_updated (Union[Unset, datetime.datetime]):
    """

    name: str
    keys: Union[
        AgentSecurityKeys,
        AwsSecurityKeys,
        AzureSecurityKeys,
        BitBucketSecurityKeys,
        CodeCommitSecurityKeys,
        ContainerRegistryKeys,
        GitHubSecurityKeys,
        GitLabSecurityKeys,
        GoogleSecurityKeys,
        K8SSecurityKeys,
        SSHSecurityKeys,
        Unset,
    ] = UNSET
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    provider: Union[Unset, CredentialsSpecProvider] = UNSET
    base_url: Union[Unset, str] = UNSET
    category: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    last_used: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    last_updated: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        keys: Union[Dict[str, Any], Unset]
        if isinstance(self.keys, Unset):
            keys = UNSET

        elif isinstance(self.keys, AwsSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, GoogleSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, GitHubSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, GitLabSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, BitBucketSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, SSHSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, K8SSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, AzureSecurityKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, ContainerRegistryKeys):
            keys = self.keys.to_dict()

        elif isinstance(self.keys, AgentSecurityKeys):
            keys = self.keys.to_dict()

        else:
            keys = self.keys.to_dict()

        id = self.id
        description = self.description
        provider: Union[Unset, str] = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.value

        base_url = self.base_url
        category = self.category
        deleted = self.deleted
        last_used: Union[Unset, str] = UNSET
        if not isinstance(self.last_used, Unset):
            last_used = self.last_used.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        last_updated: Union[Unset, str] = UNSET
        if not isinstance(self.last_updated, Unset):
            last_updated = self.last_updated.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if keys is not UNSET:
            field_dict["keys"] = keys
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if provider is not UNSET:
            field_dict["provider"] = provider
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if category is not UNSET:
            field_dict["category"] = category
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if last_used is not UNSET:
            field_dict["lastUsed"] = last_used
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if last_updated is not UNSET:
            field_dict["lastUpdated"] = last_updated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        def _parse_keys(
            data: object,
        ) -> Union[
            AgentSecurityKeys,
            AwsSecurityKeys,
            AzureSecurityKeys,
            BitBucketSecurityKeys,
            CodeCommitSecurityKeys,
            ContainerRegistryKeys,
            GitHubSecurityKeys,
            GitLabSecurityKeys,
            GoogleSecurityKeys,
            K8SSecurityKeys,
            SSHSecurityKeys,
            Unset,
        ]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_0 = AwsSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_1 = GoogleSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_2 = GitHubSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_3 = GitLabSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_4 = BitBucketSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_5 = SSHSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_5
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_6 = K8SSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_6
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_7 = AzureSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_7
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_8 = ContainerRegistryKeys.from_dict(data)

                return componentsschemas_security_keys_type_8
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_security_keys_type_9 = AgentSecurityKeys.from_dict(data)

                return componentsschemas_security_keys_type_9
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_security_keys_type_10 = CodeCommitSecurityKeys.from_dict(data)

            return componentsschemas_security_keys_type_10

        keys = _parse_keys(d.pop("keys", UNSET))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _provider = d.pop("provider", UNSET)
        provider: Union[Unset, CredentialsSpecProvider]
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = CredentialsSpecProvider(_provider)

        base_url = d.pop("baseUrl", UNSET)

        category = d.pop("category", UNSET)

        deleted = d.pop("deleted", UNSET)

        _last_used = d.pop("lastUsed", UNSET)
        last_used: Union[Unset, datetime.datetime]
        if isinstance(_last_used, Unset):
            last_used = UNSET
        else:
            last_used = isoparse(_last_used)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _last_updated = d.pop("lastUpdated", UNSET)
        last_updated: Union[Unset, datetime.datetime]
        if isinstance(_last_updated, Unset):
            last_updated = UNSET
        else:
            last_updated = isoparse(_last_updated)

        credentials_spec = cls(
            name=name,
            keys=keys,
            id=id,
            description=description,
            provider=provider,
            base_url=base_url,
            category=category,
            deleted=deleted,
            last_used=last_used,
            date_created=date_created,
            last_updated=last_updated,
        )

        credentials_spec.additional_properties = d
        return credentials_spec

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
