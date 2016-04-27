
Update aggregate
================

.. rest_method::  PUT /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Updates either or both the name and availability zone for an aggregate.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - aggregate_id: aggregate_id

Request Example
---------------

.. literalinclude:: ../samples/os-aggregates/aggregate-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-aggregates/aggregate-update-response.json
   :language: javascript



