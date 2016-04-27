
List VPN endpoint groups
========================

.. rest_method::  GET /v2.0/vpn/endpoint-groups

Lists VPN endpoint groups.


Normal response codes: 200
Error response codes:403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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

.. literalinclude:: ../samples/vpn/vpn-endpoint-groups-list-response.json
   :language: javascript





