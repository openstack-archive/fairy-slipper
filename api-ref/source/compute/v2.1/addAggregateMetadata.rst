
Create or update aggregate metadata
===================================

.. rest_method::  POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Creates or replaces metadata for an aggregate.

Specify the ``set_metadata`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - aggregate_id: aggregate_id

Request Example
---------------

.. literalinclude:: ../samples/os-aggregates/aggregate-metadata-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-aggregates/aggregate-metadata-create-response.json
   :language: javascript



