#!/usr/bin/env python
import logging
import json
import os
from subprocess import call
import sys

logging.basicConfig()

with open("terraform.tfstate") as fp:
    state = json.load(fp)

hosts = []

for module in state["modules"]:
    for key, resource in module["resources"].iteritems():
        ip_address = resource["primary"]["attributes"]["ipv4_address"]

        print key, ip_address

        os.system("echo stat | nc {} 2181".format(ip_address))
        print

        hosts.append("{}:2181".format(ip_address))

from kazoo.client import KazooClient

zk = KazooClient(hosts=",".join(hosts))
zk.start()

zk.ensure_path("/test")

zk.stop()
