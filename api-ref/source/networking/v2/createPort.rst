
Create port
===========

.. rest_method::  POST /v2.0/ports

Creates a port on a network.

To define the network in which to create the port, specify the
``network_id`` attribute in the request body.

Error response codes:201,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - opt_value: opt_value
   - name: name
   - allowed_address_pairs: allowed_address_pairs
   - admin_state_up: admin_state_up
   - network_id: network_id
   - fixed_ips: fixed_ips
   - opt_name: opt_name
   - subnet_id: subnet_id
   - device_owner: device_owner
   - tenant_id: tenant_id
   - mac_address: mac_address
   - ip_address: ip_address
   - port: port
   - security_groups: security_groups
   - device_id: device_id

Request Example
---------------

.. literalinclude:: ../samples/ports/port-create-request.json
   :language: javascript




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










