module "cloud-run" {
  source  = "GoogleCloudPlatform/cloud-run/google"
  version = "~> 0.21"

  service_name = "cal-bc-staging"
  project_id   = "cal-itp-data-infra-staging"
  location     = "us-west2"
  image        = "ghcr.io/cal-itp/cal-bc/cal-bc:development"

  env_vars = [
    {
      name  = "SECRET_KEY",
      value = random_password.cal-bc-staging-secret-key.result
    },
    {
      name  = "DATABASE_URL",
      value = "postgres://${google_sql_user.cal-bc-staging.name}:${random_password.cal-bc-staging-database.result}@//cloudsql/${google_sql_database_instance.cal-bc-staging.project}:${google_sql_database_instance.cal-bc-staging.region}:${google_sql_database_instance.cal-bc-staging.name}/${google_sql_database.cal-bc-staging.name}"
    }
  ]
}
