resource "google_cloud_run_v2_worker_pool" "cal-bc-staging-tasks" {
  name                = "cal-bc-staging-tasks"
  location            = "us-west2"
  deletion_protection = false

  template {
    service_account = data.terraform_remote_state.iam.outputs.google_service_account_cal-bc-service-account_email

    volumes {
      name = "cloudsql"

      cloud_sql_instance {
        instances = [google_sql_database_instance.cal-bc-staging.connection_name]
      }
    }

    containers {
      image   = "us-west2-docker.pkg.dev/cal-itp-data-infra-staging/ghcr/cal-itp/cal-bc/cal-bc:${var.image_tag}"
      command = ["uv", "run", "--no-sync", "manage.py", "db_worker"]

      resources {
        limits = {
          "cpu"    = "1"
          "memory" = "1Gi"
        }
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
}
