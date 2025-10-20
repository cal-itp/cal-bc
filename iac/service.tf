module "cloud-run" {
  source  = "GoogleCloudPlatform/cloud-run/google"
  version = "~> 0.21"

  service_name = "cal-bc-staging"
  project_id   = "cal-itp-data-infra-staging"
  location     = "us-west2"
  image        = "us-west2-docker.pkg.dev/cal-itp-data-infra-staging/ghcr/cal-itp/cal-bc/cal-bc:development"

  service_account_email = data.terraform_remote_state.iam.outputs.google_service_account_cal-bc-service-account_email

  ports = {
    name = "http1"
    port = 8000
  }

  env_secret_vars = [
    {
      name = "SECRET_KEY"
      value_from = [
        {
          secret_key_ref = {
            name = google_secret_manager_secret.cal-bc-staging-secret-key.secret_id
            key  = "latest"
          }
        }
      ]
    },
    {
      name = "DATABASE_URL"
      value_from = [
        {
          secret_key_ref = {
            name = google_secret_manager_secret.cal-bc-staging-database-url.secret_id
            key  = "latest"
          }
        }
      ]
    }
  ]
}
