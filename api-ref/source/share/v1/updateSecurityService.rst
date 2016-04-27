
Update security service
=======================

.. rest_method::  PUT /v2/{tenant_id}/security-services/{security_service_id}

Updates a security service.

If the security service is in ``active`` state, you can update only
the ``name`` and ``description`` attributes. A security service in
``active`` state is attached to a share network with an associated
share server.


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
   - security_service_id: security_service_id

Request Example
---------------

.. literalinclude:: ../samples/manila-security-service-update-request.json
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

.. literalinclude:: ../samples/manila-security-service-update-response.json
   :language: javascript



