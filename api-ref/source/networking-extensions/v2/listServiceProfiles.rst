
List service profiles
=====================

.. rest_method::  GET /v2.0/service_profiles

Lists all service profiles visible for the tenant account.

The list can be empty.

Standard query parameters are supported on the URI.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - driver: driver
   - enabled: enabled
   - metainfo: metainfo
   - service_profiles: service_profiles
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/flavors/service-profiles-list-response.json
   :language: javascript




