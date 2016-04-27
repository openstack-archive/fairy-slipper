
Show flavor details
===================

.. rest_method::  GET /v2.0/flavors/{flavor_id}

Shows details for a flavor.

This operation returns a flavor object by ID. If you are not an
administrative user and the flavor object is not visible to your
tenant account, the service returns the HTTP ``Forbidden (403)``
response code.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - flavor_id: flavor_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - enabled: enabled
   - service_profiles: service_profiles
   - service_type: service_type
   - flavor: flavor
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/flavors/flavor-show-response.json
   :language: javascript






