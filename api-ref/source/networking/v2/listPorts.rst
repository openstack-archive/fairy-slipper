
List ports
==========

.. rest_method::  GET /v2.0/ports

Lists ports to which the tenant has access.

Default policy settings return only those ports that are owned by
the tenant who submits the request, unless the request is submitted
by a user with administrative rights. Users can control which
attributes are returned by using the fields query parameter. You
can use query parameters to filter the response.For information,
see `Filtering and Column Selection <https://wiki.openstack.org/wik
i/Neutron/APIv2-specification#Filtering_and_Column_Selection>`_.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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
   - ports: ports
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

.. literalinclude:: ../samples/ports/ports-list-response.json
   :language: javascript




