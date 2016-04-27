
List security services with details
===================================

.. rest_method::  GET /v2/{tenant_id}/security-services/detail

Lists all security services with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



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

.. literalinclude:: ../samples/manila-security-services-list-detailed-response.json
   :language: javascript



