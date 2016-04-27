
Create QoS policy
=================

.. rest_method::  POST /v2.0/qos/policies

Creates a QoS policy.

Creates a QoS policy by using the configuration that you define in
the request object. A response object is returned. The object
contains a unique ID.

If the caller is not an administrative user, this call returns the
HTTP ``Forbidden (403)`` response code.

Users with an administrative role can create policies on behalf of
other tenants by specifying a tenant UUID that is different than
their own.

Error response codes:201,404,409,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - policy: policy
   - shared: shared
   - type: type
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/qos/policy-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - policy: policy
   - shared: shared
   - id: id
   - name: name











