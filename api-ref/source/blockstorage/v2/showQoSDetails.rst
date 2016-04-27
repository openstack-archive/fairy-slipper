
Show QoS specification details
==============================

.. rest_method::  GET /v2/{tenant_id}/qos-specs/{qos_id}

Shows details for a QoS specification.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - qos_id: qos_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - links: links
   - id: id
   - qos_specs: qos_specs
   - consumer: consumer
   - specs: specs




Response Example
----------------

.. literalinclude:: ../samples/qos-specs/qos-show-response.json
   :language: javascript










