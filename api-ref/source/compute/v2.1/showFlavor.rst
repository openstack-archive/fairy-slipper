
Show flavor details
===================

.. rest_method::  GET /v2.1/{tenant_id}/flavors/{flavor_id}

Shows details for a flavor.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - flavor_id: flavor_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/flavors/flavor-show-response.json
   :language: javascript



