
Associate flavor
================

.. rest_method::  POST /v2.0/flavors/{flavor_id}/service_profiles

Associate a flavor with a service profile.

A flavor can be associated with more than one profile.

Will return ``409 Conflict`` if association already exists.

Error response codes:201,404,403,401,400,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_profile: service_profile
   - id: id
   - flavor_id: flavor_id

Request Example
---------------

.. literalinclude:: ../samples/flavors/flavor-associate-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - service_profile: service_profile
   - id: id










