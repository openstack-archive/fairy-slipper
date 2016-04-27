
Create QoS specification
========================

.. rest_method::  POST /v2/{tenant_id}/qos-specs

Creates a QoS specification.

Specify one or more key and value pairs in the request body.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - qos_specs: qos_specs
   - consumer: consumer
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/qos-specs/qos-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - links: links
   - id: id
   - qos_specs: qos_specs
   - consumer: consumer
   - specs: specs





