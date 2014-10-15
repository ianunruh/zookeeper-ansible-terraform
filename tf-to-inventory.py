#!/usr/bin/env python
import json

hosts = {}
groups = {}

with open("terraform.tfstate") as fp:
    state = json.load(fp)

for module in state["modules"]:
    for key, resource in module["resources"].iteritems():
        resource_type, group_name, index = key.split(".")
        
        index = int(index)
        attributes = resource["primary"]["attributes"]
        name = attributes["name"]

        if resource_type == "digitalocean_droplet" and attributes["status"] == "active":
            hosts[name] = attributes["ipv4_address"]
            groups.setdefault(group_name, {})[name] = {
                "index": index,
                "nz_index": index + 1,
            }

with open("hosts", "w") as fp:
    for host, ip_address in hosts.iteritems():
        fp.write("{} ansible_ssh_host={} ansible_ssh_user=root\n".format(host, ip_address))

    for group, hosts in groups.iteritems():
        fp.write("[{}]\n".format(group))
        for host, variables in hosts.iteritems():
            fp.write(host)
            for k, v in variables.iteritems():
                fp.write(" {}={}".format(k, v))
            fp.write("\n")
