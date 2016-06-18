#!/usr/bin/env python
import json
import re

with open('terraform.tfstate') as tf_data:
  data = json.load(tf_data)

hosts = {}

for x, y in data["modules"][0]["resources"].iteritems():
  if re.search("^openstack_compute_instance_v2", x):

      ip = y["primary"]["attributes"]["access_ip_v4"]
      name = y["primary"]["attributes"]["name"]
      role = y["primary"]["attributes"]["metadata.role"]

      hosts[name] = []
      hosts[name].append(ip)

      if role not in hosts:
        hosts[role] = []
      hosts[role].append(ip)

print json.dumps(hosts)

