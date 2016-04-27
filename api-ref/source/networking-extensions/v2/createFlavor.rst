
Create flavor
=============

.. rest_method::  POST /v2.0/flavors

Creates a flavor.

This operation establishes a new flavor.

The service_type to which the flavor applies is a required
parameter. The corresponding service plugin must have been
activated as part of the configuration. See `Service providers
<http://developer.openstack.org/api-ref-networking-v2.html#service-
type>`_ for how to see currently loaded service types. Additionally
the service plugin needs to support the use of flavors. For
example, the LOADBALANCERV2 service type using the LBaaSv2 API
currently supports Neutron service flavors.

Creation currently limited to administrators. Other users will
receive a ``Forbidden 403`` response code with a response body
NeutronError message expressing that creation is disallowed by
policy.

Until one or more service profiles are associated with the flavor
by the operator, attempts to use the flavor during resource
creations will currently return a ``Not Found 404`` with a response
body that indicates no service profile could be found.

If the API cannot fulfill the request due to insufficient data or
data that is not valid, the service returns the HTTP ``Bad Request
(400)`` response code with information about the failure in the
response body. Validation errors require that you correct the error
and submit the request again.

Error response codes:201,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - service_type: service_type
   - flavor: flavor
   - enabled: enabled
   - description: description
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/flavors/flavor-create-request.json
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








