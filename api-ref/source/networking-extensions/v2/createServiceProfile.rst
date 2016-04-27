
Create service profile
======================

.. rest_method::  POST /v2.0/service_profiles

Creates a service profile.

This operation establishes a new service profile that can be
associated with one or more flavors.

Either metadata or a driver is required.

If a driver is specified but does not exist, call will return a
``Not found 404`` error with the response body explaining that the
driver could not be found.

Creation currently limited to administrators. Other users will
receive a ``Forbidden 403`` response code with a response body
NeutronError message expressing that creation is disallowed by
policy.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, the service returns the HTTP ``Bad Request
(400)`` response code with information about the failure in the
response body. Validation errors require that you correct the error
and submit the request again.

Error response codes:201,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_profile: service_profile
   - enabled: enabled
   - driver: driver
   - description: description
   - metainfo: metainfo

Request Example
---------------

.. literalinclude:: ../samples/flavors/service-profile-create-request.json
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








