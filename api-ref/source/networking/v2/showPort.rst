
Show port details
=================

.. rest_method::  GET /v2.0/ports/{port_id}

Shows details for a port.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - port_id: port_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - opt_value: opt_value
   - status: status
   - name: name
   - allowed_address_pairs: allowed_address_pairs
   - admin_state_up: admin_state_up
   - network_id: network_id
   - ip_address: ip_address
   - extra_dhcp_opts: extra_dhcp_opts
   - opt_name: opt_name
   - updated_at: updated_at
   - id: id
   - port: port
   - subnet_id: subnet_id
   - device_owner: device_owner
   - tenant_id: tenant_id
   - mac_address: mac_address
   - port_security_enabled: port_security_enabled
   - fixed_ips: fixed_ips
   - created_at: created_at
   - security_groups: security_groups
   - device_id: device_id




Response Example
----------------

.. literalinclude:: ../samples/ports/port-show-response.json
   :language: javascript





