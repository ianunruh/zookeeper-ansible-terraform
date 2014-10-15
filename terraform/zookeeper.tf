provider "digitalocean" {
  token = "${var.digitalocean_token}"
}

resource "digitalocean_droplet" "zk" {
  count = "${var.cluster_size}"

  name = "zk-demo-${count.index}"

  ssh_keys = ["${var.digitalocean_ssh_key}"]
  
  region = "nyc3"

  image = "ubuntu-14-04-x64"
  size = "512mb"
}
