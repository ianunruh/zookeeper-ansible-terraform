#!/bin/bash
set -eux

python clean-known-hosts.py

terraform destroy terraform
