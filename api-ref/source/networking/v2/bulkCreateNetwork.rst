
Bulk create networks
====================

.. rest_method::  POST /v2.0/networks

Creates multiple networks in a single request.

In the request body, specify a list of networks.

The bulk create operation is always atomic. Either all or no
networks in the request body are created.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - router:external: router:external
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - port_security_enabled: port_security_enabled
   - shared: shared
   - networks: networks

Request Example
---------------

.. literalinclude:: ../samples/networks/networks-bulk-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - router:external: router:external
   - subnets: subnets
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - mtu: mtu
   - shared: shared
   - id: id
   - port_security_enabled: port_security_enabled
   - networks: networks







