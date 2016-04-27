
Update flavor
=============

.. rest_method::  PUT /v2.0/flavors/{flavor_id}

Updates a flavor.

The service_type cannot be updated as there may be associated
service profiles and consumers depending on the value.


Normal response codes: 200
Error response codes:404,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - flavor: flavor
   - enabled: enabled
   - description: description
   - name: name
   - flavor_id: flavor_id

Request Example
---------------

.. literalinclude:: ../samples/flavors/flavor-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/flavors/flavor-update-response.json
   :language: javascript







