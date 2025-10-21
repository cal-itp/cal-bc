resource "google_secret_manager_secret" "cal-bc-staging-secret-key" {
  secret_id = "cal-bc-staging-secret-key"
  replication {
    user_managed {
      replicas {
        location = "us-west2"
      }
    }
  }
}

resource "google_secret_manager_secret_version" "cal-bc-staging-secret-key" {
  secret         = google_secret_manager_secret.cal-bc-staging-secret-key.name
  secret_data_wo = random_password.cal-bc-staging-secret-key.result
}

resource "google_secret_manager_secret" "cal-bc-staging-database-url" {
  secret_id = "cal-bc-staging-database-url"
  replication {
    user_managed {
      replicas {
        location = "us-west2"
      }
    }
  }
}

resource "google_secret_manager_secret_version" "cal-bc-staging-database-url" {
  secret         = google_secret_manager_secret.cal-bc-staging-database-url.name
  secret_data_wo = "postgres://${google_sql_user.cal-bc-staging.name}:${random_password.cal-bc-staging-database.result}@//cloudsql/${google_sql_database_instance.cal-bc-staging.project}:${google_sql_database_instance.cal-bc-staging.region}:${google_sql_database_instance.cal-bc-staging.name}/${google_sql_database.cal-bc-staging.name}"
}

resource "google_secret_manager_secret" "cal-bc-staging-azure-auth-client-id" {
  secret_id = "cal-bc-staging-azure-auth-client-id"
  replication {
    user_managed {
      replicas {
        location = "us-west2"
      }
    }
  }
}

resource "google_secret_manager_secret_version" "cal-bc-staging-azure-auth-client-id" {
  secret = google_secret_manager_secret.cal-bc-staging-azure-auth-client-id.name
}

resource "google_secret_manager_secret" "cal-bc-staging-azure-auth-client-secret" {
  secret_id = "cal-bc-staging-azure-auth-client-secret"
  replication {
    user_managed {
      replicas {
        location = "us-west2"
      }
    }
  }
}

resource "google_secret_manager_secret_version" "cal-bc-staging-azure-auth-client-secret" {
  secret = google_secret_manager_secret.cal-bc-staging-azure-auth-client-secret.name
}

resource "google_secret_manager_secret" "cal-bc-staging-azure-auth-directory-id" {
  secret_id = "cal-bc-staging-azure-auth-directory-id"
  replication {
    user_managed {
      replicas {
        location = "us-west2"
      }
    }
  }
}

resource "google_secret_manager_secret_version" "cal-bc-staging-azure-auth-directory-id" {
  secret = google_secret_manager_secret.cal-bc-staging-azure-auth-directory-id.name
}

resource "google_secret_manager_secret" "cal-bc-staging-cloudrun-service-urls" {
  secret_id = "cal-bc-staging-cloudrun-service-urls"
  replication {
    user_managed {
      replicas {
        location = "us-west2"
      }
    }
  }
}

resource "google_secret_manager_secret_version" "cal-bc-staging-cloudrun-service-urls" {
  secret      = google_secret_manager_secret.cal-bc-staging-cloudrun-service-urls.name
  secret_data = join(",", concat(google_cloud_run_v2_service.cal-bc-staging.urls, ["https://${local.domain}"]))
}
