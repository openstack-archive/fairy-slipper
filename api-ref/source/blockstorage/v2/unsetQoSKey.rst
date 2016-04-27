
Unset keys in QoS specification
===============================

.. rest_method::  PUT /v2/{tenant_id}/qos-specs/{qos_id}/delete_keys

Unsets keys in a QoS specification.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - keys: keys
   - tenant_id: tenant_id
   - qos_id: qos_id

Request Example
---------------

.. literalinclude:: ../samples/qos-specs/qos-unset-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: 
   :language: javascript



