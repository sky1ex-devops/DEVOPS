job "client" {
  datacenters = ["dc1"]

  group "client" {
    count = 2

    task "agent-task-service" {
      driver = "docker"

      config {
        image = "hashicorp/nomad"
      }

      resources {
        cpu    = 300
        memory = 100

        network {
          mbits = 10
          port "http" {}
        }
      }

      template {
        data = <<EOF
        log_level    = "DEBUG"
        data_dir     = "/tmp/nomad-client{{ env "NOMAD_ALLOC_INDEX" }}"
        name         = "client-{{ env "NOMAD_ALLOC_INDEX" }}"
        enable_debug = true
        client {
          enabled = true
          servers = ["127.0.0.1:4647"]
          options {
          "driver.raw_exec.enable" = "1"
        }
      }

ports {
  http = {{ env "NOMAD_PORT_http" }}
}
	 EOF

        destination = "local/config/client.hcl"
      }
    }
  }
}