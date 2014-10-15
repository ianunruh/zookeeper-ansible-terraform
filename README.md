# zookeeper-ansible-terraform

Deploys a ZooKeeper cluster on DigitalOcean, using Ansible and Terraform

## Usage

1. [Install Ansible](http://docs.ansible.com/intro_installation.html)
2. [Install Terraform](http://www.terraform.io/intro/getting-started/install.html)
3. [Get a personal access token from DigitalOcean](https://cloud.digitalocean.com/settings/applications)
4. [Add an SSH key](https://cloud.digitalocean.com/ssh_keys)

Retrieve the ID of your SSH key using the following command.

```bash
TOKEN=YOUR TOKEN HERE
curl -X GET "https://api.digitalocean.com/v2/account/keys" -H "Authorization: Bearer $TOKEN" | python -m json.tool
```

Now, create a file named `terraform.tfvars` in this directory that looks like the following.

```
digitalocean_token = "YOUR TOKEN HERE"
digitalocean_ssh_key = "YOUR SSH KEY ID HERE"
```

Finally, use `launch.sh` to bring up the cluster. You may have to run `launch.sh` several times, as the droplets can take some time to be ready.

After the cluster is deployed, use `test-zk.py` to check the status of ZooKeeper.
