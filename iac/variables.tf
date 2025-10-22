data "terraform_remote_state" "iam" {
  backend = "gcs"

  config = {
    bucket = "calitp-staging-gcp-components-tfstate"
    prefix = "cal-itp-data-infra-staging/iam"
  }
}

resource "random_password" "cal-bc-staging-secret-key" {
  special = false
  length  = 50
}

resource "random_password" "cal-bc-staging-database" {
  special = false
  length  = 32
}

locals {
  domain = "cal-bc-staging.dds.dot.ca.gov"
}

variable "image_tag" {
  type        = string
  description = "The tag used for image deployment"
  default     = "latest"
}
