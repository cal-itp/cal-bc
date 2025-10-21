resource "google_cloud_run_v2_service" "cal-bc-staging" {
  name                = "cal-bc-staging"
  location            = "us-west2"
  deletion_protection = false
  ingress             = "INGRESS_TRAFFIC_ALL"

  traffic {
    type    = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
    percent = 100
  }

  scaling {
    min_instance_count = 1
  }

  template {
    service_account = data.terraform_remote_state.iam.outputs.google_service_account_cal-bc-service-account_email

    volumes {
      name = "cloudsql"
      cloud_sql_instance {
        instances = [google_sql_database_instance.cal-bc-staging.connection_name]
      }
    }

    containers {
      image = "us-west2-docker.pkg.dev/cal-itp-data-infra-staging/ghcr/cal-itp/cal-bc/cal-bc:development"
      ports {
        container_port = 8000
      }

      volume_mounts {
        name       = "cloudsql"
        mount_path = "/cloudsql"
      }

      env {
        name = "SECRET_KEY"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.cal-bc-staging-secret-key.secret_id
            version = "latest"
          }
        }
      }

      env {
        name = "DATABASE_URL"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.cal-bc-staging-database-url.secret_id
            version = "latest"
          }
        }
      }

      env {
        name = "AZURE_AUTH__CLIENT_ID"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.cal-bc-staging-azure-auth-client-id.secret_id
            version = "latest"
          }
        }
      }

      env {
        name = "AZURE_AUTH__CLIENT_SECRET"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.cal-bc-staging-azure-auth-client-secret.secret_id
            version = "latest"
          }
        }
      }

      env {
        name = "AZURE_AUTH__DIRECTORY_ID"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.cal-bc-staging-azure-auth-directory-id.secret_id
            version = "latest"
          }
        }
      }

      env {
        name = "CLOUDRUN_SERVICE_URLS"
        value_source {
          secret_key_ref {
            secret  = google_secret_manager_secret.cal-bc-staging-cloudrun-service-urls.secret_id
            version = "latest"
          }
        }
      }
    }
  }
}

resource "google_cloud_run_service_iam_binding" "cal-bc-staging" {
  location = google_cloud_run_v2_service.cal-bc-staging.location
  service  = google_cloud_run_v2_service.cal-bc-staging.name
  role     = "roles/run.invoker"
  members  = ["allUsers"]
}

resource "google_compute_region_network_endpoint_group" "cal-bc-staging" {
  name                  = "cal-bc-staging"
  network_endpoint_type = "SERVERLESS"
  region                = google_cloud_run_v2_service.cal-bc-staging.location
  cloud_run {
    service = google_cloud_run_v2_service.cal-bc-staging.name
  }
}

resource "google_compute_global_address" "cal-bc-staging" {
  name = "cal-bc-staging-address"
}

module "lb-http" {
  source  = "GoogleCloudPlatform/lb-http/google//modules/serverless_negs"
  version = "~> 13.2"

  name    = "cal-bc-staging"
  project = "cal-itp-data-infra-staging"

  ssl                             = true
  managed_ssl_certificate_domains = [local.domain]
  https_redirect                  = true

  address        = google_compute_global_address.cal-bc-staging.address
  create_address = false

  backends = {
    default = {
      description = null

      groups = []
      serverless_neg_backends = [
        {
          "region" : "us-west2",
          "type" : "cloud-run",
          "service" : {
            "name" : google_cloud_run_v2_service.cal-bc-staging.name
          }
        }
      ]

      health_check = {
        request_path = "/"
        protocol     = "HTTP"
        port         = 80
      }

      enable_cdn = false

      iap_config = {
        enable = false
      }

      log_config = {
        enable = false
      }
    }
  }
}
