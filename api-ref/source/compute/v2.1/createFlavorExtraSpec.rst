
Create extra specs for a flavor
===============================

.. rest_method::  POST /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs

Creates extra specs for a flavor, by ID.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - flavor_id: flavor_id

Request Example
---------------

.. literalinclude:: ../samples/os-flavor-extra-specs/flavor-extra-spec-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-flavor-extra-specs/flavor-extra-spec-create-response.json
   :language: javascript



