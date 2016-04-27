
Create security service
=======================

.. rest_method::  POST /v2/{tenant_id}/security-services

Creates a security service.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain: domain
   - description: description
   - dns_ip: dns_ip
   - server: server
   - user: user
   - password: password
   - type: type
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-security-service-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - domain: domain
   - project_id: project_id
   - name: name
   - updated_at: updated_at
   - created_at: created_at
   - dns_ip: dns_ip
   - server: server
   - user: user
   - password: password
   - type: type
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/manila-security-service-create-response.json
   :language: javascript



