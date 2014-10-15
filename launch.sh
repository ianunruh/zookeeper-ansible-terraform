#!/bin/bash
set -eux

terraform apply terraform

python tf-to-inventory.py

export ANSIBLE_HOST_KEY_CHECKING=False

ansible-playbook -i hosts playbook.yml
