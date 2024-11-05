log_level = "DEBUG"

data_dir = "/opt/nomad"

server {
  enabled = true

  bootstrap_expect = 1
}

client {
  enabled = true

  options {
    "docker.privileged.enabled" = "true"
  }
}