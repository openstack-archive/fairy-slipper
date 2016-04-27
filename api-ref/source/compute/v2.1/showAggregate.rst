
Show aggregate details
======================

.. rest_method::  GET /v2.1/{tenant_id}/os-aggregates/{aggregate_id}

Shows details for an aggregate. Details include hosts and metadata.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - aggregate_id: aggregate_id

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

.. literalinclude:: ../samples/os-aggregates/aggregate-show-response.json
   :language: javascript



