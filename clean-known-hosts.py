#!/usr/bin/env python
import json
import os
from subprocess import call
import sys

if not os.path.exists("terraform.tfstate"):
    sys.exit(0)

with open("terraform.tfstate") as fp:
    state = json.load(fp)

for module in state["modules"]:
    for key, resource in module["resources"].iteritems():
        print "++", key
        try:
            call(["ssh-keygen", "-R", resource["primary"]["attributes"]["ipv4_address"]])
        except:
            pass
