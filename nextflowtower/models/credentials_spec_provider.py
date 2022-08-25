from enum import Enum


class CredentialsSpecProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GOOGLE = "google"
    GITHUB = "github"
    GITLAB = "gitlab"
    BITBUCKET = "bitbucket"
    SSH = "ssh"
    K8S = "k8s"
    CONTAINER_REG = "container-reg"
    TW_AGENT = "tw-agent"
    CODECOMMIT = "codecommit"

    def __str__(self) -> str:
        return str(self.value)
