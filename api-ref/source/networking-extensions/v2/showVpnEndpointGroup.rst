
Show VPN endpoint group
=======================

.. rest_method::  GET /v2.0/vpn/endpoint-groups/{endpoint_group_id}

Shows details for a VPN endpoint group.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - endpoint_group_id: endpoint_group_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - endpoints: endpoints
   - type: type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/vpn/vpn-endpoint-group-show-response.json
   :language: javascript






