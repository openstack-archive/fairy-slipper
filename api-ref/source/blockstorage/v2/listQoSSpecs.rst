
List QoS specs
==============

.. rest_method::  GET /v2/{tenant_id}/qos-specs

Lists quality of service (QoS) specifications.


Normal response codes: 200
Error response codes:300,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - sort_key: sort_key
   - sort_dir: sort_dir
   - limit: limit
   - marker: marker



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - specs: specs
   - qos_specs: qos_specs
   - consumer: consumer
   - id: id
   - name: name





Response Example
----------------

.. literalinclude:: ../samples/qos-specs/qos-list-response.json
   :language: javascript



