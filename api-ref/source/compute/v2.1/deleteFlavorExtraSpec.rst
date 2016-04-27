
Delete an extra spec for a flavor
=================================

.. rest_method::  DELETE /v2.1/{tenant_id}/flavors/{flavor_id}/os-extra_specs/{flavor_extra_spec_key}

Deletes an extra spec, by key, for a flavor, by ID.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - flavor_id: flavor_id
   - flavor_extra_spec_key: flavor_extra_spec_key






Response Example
----------------

.. literalinclude:: 
   :language: javascript



