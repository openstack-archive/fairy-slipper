
Update VPN endpoint group
=========================

.. rest_method::  PUT /v2.0/vpn/endpoint-groups/{endpoint_group_id}

Updates settings for a VPN endpoint group.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - name: name
   - endpoint_group_id: endpoint_group_id

Request Example
---------------

.. literalinclude:: ../samples/vpn/vpn-endpoint-group-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/vpn/vpn-endpoint-group-update-response.json
   :language: javascript






