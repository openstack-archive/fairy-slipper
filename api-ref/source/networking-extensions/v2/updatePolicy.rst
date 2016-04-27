
Update QoS policy
=================

.. rest_method::  PUT /v2.0/qos/policies/{policy_id}

Updates a QoS policy.

If the request is valid, the service returns the ``Accepted (202)``
response code.


Normal response codes: 200
Error response codes:400,401,413,503,500,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - policy: policy
   - shared: shared
   - type: type
   - name: name
   - policy_id: policy_id

Request Example
---------------

.. literalinclude:: ../samples/qos/policy-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/qos/policy-update-response.json
   :language: javascript








