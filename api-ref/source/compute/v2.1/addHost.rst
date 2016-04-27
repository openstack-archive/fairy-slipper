
Add host
========

.. rest_method::  POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Adds a host to an aggregate.

Specify the ``add_host`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - aggregate_id: aggregate_id

Request Example
---------------

.. literalinclude:: ../samples/os-aggregates/aggregate-add-host-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-aggregates/aggregate-add-host-response.json
   :language: javascript



