
Create policy
=============

.. rest_method::  POST /v1/policies

Creates a policy.

Error response codes:201,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - policy: policy
   - spec: spec
   - cooldown: cooldown
   - name: name
   - level: level

Request Example
---------------

.. literalinclude:: ../samples/policy-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - location: location
   - policy: policy





