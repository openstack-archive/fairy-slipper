
Show service profile details
============================

.. rest_method::  GET /v2.0/service_profiles/{profile_id}

Shows details for a service profile.

This operation returns a service profile object by ID. If you are
not an administrative user and the object is not visible to your
tenant account, the service returns the HTTP ``Forbidden (403)``
response code.


Normal response codes: 200
Error response codes:404,403,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - profile_id: profile_id



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

.. literalinclude:: ../samples/flavors/service-profile-show-response.json
   :language: javascript






