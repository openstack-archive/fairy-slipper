
Show security service details
=============================

.. rest_method::  GET /v2/{tenant_id}/security-services/{security_service_id}

Shows details for a security service.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - security_service_id: security_service_id



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

.. literalinclude:: ../samples/manila-security-service-show-response.json
   :language: javascript



