resource "google_sql_database_instance" "cal-bc-staging" {
  name             = "cal-bc-staging"
  database_version = "POSTGRES_18"
  region           = "us-west2"
  settings {
    tier = "db-g1-small"
    maintenance_window {
      day  = 1
      hour = 0
    }
  }
  deletion_protection = true
}

resource "google_sql_database" "cal-bc-staging" {
  name     = "cal-bc-staging"
  instance = google_sql_database_instance.cal-bc-staging.name
}

resource "google_sql_user" "cal-bc-staging" {
  name        = "cal-bc-staging"
  instance    = google_sql_database_instance.cal-bc-staging.name
  password_wo = random_password.cal-bc-staging-database.result
}
