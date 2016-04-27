
List aggregates
===============

.. rest_method::  GET /v2.1/{tenant_id}/os-aggregates

Lists all aggregates. Includes the ID, name, and availability zone for each aggregate.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-aggregates/aggregate-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-aggregates/aggregates-list-response.json
   :language: javascript



