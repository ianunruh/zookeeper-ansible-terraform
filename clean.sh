#!/bin/bash
set -eux

python clean-known-hosts.py

terraform destroy -force terraform
