provider "google" {
  project = "cal-itp-data-infra-staging"
}

terraform {
  required_providers {
    google = {
      version = "~> 7.39.0"
    }
  }

  backend "gcs" {
    bucket = "calitp-staging-gcp-components-tfstate"
    prefix = "cal-itp-data-infra-staging/cal-bc"
  }
}
