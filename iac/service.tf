resource "google_cloud_run_v2_service" "cal-bc-staging" {
  name                = "cal-bc-staging"
  location            = "us-west2"
  deletion_protection = false
  ingress             = "INGRESS_TRAFFIC_ALL"

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
    }
  }

  traffic {
    type    = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
    percent = 100
  }
}

resource "google_cloud_run_service_iam_binding" "cal-bc-staging" {
  location = google_cloud_run_v2_service.cal-bc-staging.location
  service  = google_cloud_run_v2_service.cal-bc-staging.name
  role     = "roles/run.invoker"
  members  = ["allUsers"]
}
