
Remove host
===========

.. rest_method::  POST /v2.1/{tenant_id}/os-aggregates/{aggregate_id}/action

Removes a host from an aggregate.

Specify the ``remove_host`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - aggregate_id: aggregate_id

Request Example
---------------

.. literalinclude:: ../samples/os-aggregates/aggregate-remove-host-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-aggregates/aggregate-remove-host-response.json
   :language: javascript



