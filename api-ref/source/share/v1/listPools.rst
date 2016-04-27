
List back-end storage pools
===========================

.. rest_method::  GET /v2/{tenant_id}/scheduler-stats/pools

Lists all back-end storage pools.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - host: host
   - name: name
   - pool: pool
   - backend: backend




Response Example
----------------

.. literalinclude:: ../samples/manila-pools-list-response.json
   :language: javascript



