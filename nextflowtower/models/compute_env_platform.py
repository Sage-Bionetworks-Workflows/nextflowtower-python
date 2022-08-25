from enum import Enum


class ComputeEnvPlatform(str, Enum):
    AWS_BATCH = "aws-batch"
    GOOGLE_LIFESCIENCES = "google-lifesciences"
    AZURE_BATCH = "azure-batch"
    K8S_PLATFORM = "k8s-platform"
    EKS_PLATFORM = "eks-platform"
    GKE_PLATFORM = "gke-platform"
    UGE_PLATFORM = "uge-platform"
    SLURM_PLATFORM = "slurm-platform"
    LSF_PLATFORM = "lsf-platform"
    ALTAIR_PLATFORM = "altair-platform"

    def __str__(self) -> str:
        return str(self.value)
