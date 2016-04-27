
Update port
===========

.. rest_method::  PUT /v2.0/ports/{port_id}

Updates a port.

You can update information for a port, such as its symbolic name
and associated IPs. When you update IPs for a port, any previously
associated IPs are removed, returned to the respective subnet
allocation pools, and replaced by the IPs in the request body.
Therefore, this operation replaces the ``fixed_ip`` attribute when
you specify it in the request body. If the updated IP addresses are
not valid or are already in use, the operation fails and the
existing IP addresses are not removed from the port.

When you update security groups for a port and the operation
succeeds, any associated security groups are removed and replaced
by the security groups in the request body. Therefore, this
operation replaces the ``security_groups`` attribute when you
specify it in the request body. If the security groups are not
valid, the operation fails and the existing security groups are not
removed from the port.


Normal response codes: 200
Error response codes:404,403,401,400,409,


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
   - port_id: port_id

Request Example
---------------

.. literalinclude:: ../samples/ports/port-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/ports/port-update-response.json
   :language: javascript








