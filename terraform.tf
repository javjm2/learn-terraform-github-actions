terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.40.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "~> 3.4.3"
    }

    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0.5"
    }

    cloudinit = {
      source  = "hashicorp/cloudinit"
      version = "~> 2.3.4"
    }
  }

  required_version = "~> 1.3"

  cloud {
    organization = "JTestOrg"

    workspaces {
      name = "pc-learn-terraform"
    }
  }
}