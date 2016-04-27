
Create VPN endpoint group
=========================

.. rest_method::  POST /v2.0/vpn/endpoint-groups

Creates a VPN endpoint group.

The endpoint group contains one or more endpoints of a specific
type that you can use to create a VPN connections.

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - endpoints: endpoints
   - type: type
   - description: description
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/vpn/vpn-endpoint-group-create-request.json
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







