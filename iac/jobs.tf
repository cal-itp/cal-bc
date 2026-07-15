resource "google_cloud_run_v2_job" "cal-bc-staging-manage" {
  name                = "cal-bc-staging-manage"
  location            = "us-west2"
  deletion_protection = false

  template {
    template {
      service_account = data.terraform_remote_state.iam.outputs.google_service_account_cal-bc-service-account_email
      max_retries     = 0

      volumes {
        name = "cloudsql"

        cloud_sql_instance {
          instances = [google_sql_database_instance.cal-bc-staging.connection_name]
        }
      }

      containers {
        image   = "us-west2-docker.pkg.dev/cal-itp-data-infra-staging/ghcr/cal-itp/cal-bc/cal-bc:${var.image_tag}"
        command = ["uv", "run", "--no-sync", "manage.py"]
        args    = ["help"]

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
  }
}
