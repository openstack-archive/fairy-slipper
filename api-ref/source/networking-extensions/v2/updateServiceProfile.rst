
Update service profile
======================

.. rest_method::  PUT /v2.0/service_profiles/{profile_id}

Updates a service profile.


Normal response codes: 200
Error response codes:404,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_profile: service_profile
   - enabled: enabled
   - driver: driver
   - description: description
   - metainfo: metainfo
   - profile_id: profile_id

Request Example
---------------

.. literalinclude:: ../samples/flavors/service-profile-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - driver: driver
   - enabled: enabled
   - metainfo: metainfo
   - service_profile: service_profile
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/flavors/service-profile-update-response.json
   :language: javascript







