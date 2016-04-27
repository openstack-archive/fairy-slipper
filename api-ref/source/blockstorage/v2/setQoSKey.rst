
Set keys in QoS specification
=============================

.. rest_method::  PUT /v2/{tenant_id}/qos-specs/{qos_id}

Sets keys in a QoS specification.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - qos_specs: qos_specs
   - specs: specs
   - tenant_id: tenant_id
   - qos_id: qos_id

Request Example
---------------

.. literalinclude:: ../samples/qos-specs/qos-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/qos-specs/qos-update-response.json
   :language: javascript



