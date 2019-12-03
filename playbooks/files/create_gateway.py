#!/usr/bin/env python3

import openstack
from otcextensions import sdk

openstack.enable_logging(True, http_debug=True)

# An 'otc' is a cloud connection with name 'otc' configured in the clouds.yaml
conn = openstack.connect()

# Register OTC Extensions
#sdk.register_otc_extensions(conn)

name = 'tino-nat-sdk-testing'
router_id = '26ca2783-dc40-4e3a-95b1-5a0756441e12'
internal_network_id = 'ad7b92c2-9f55-4ddf-90b0-8a1c98d21b21'
spec = '1'
tenant_id = '16d53a84a13b49529d2e2c3646691288'
description = 'I am a new NAT Gateway for Testing purposes'
#admin_state_up = False


response = conn.nat.create_gateway(name=name, router_id=router_id, internal_network_id=internal_network_id, spec=spec, tenant_id=tenant_id, description=description)
print(response)
