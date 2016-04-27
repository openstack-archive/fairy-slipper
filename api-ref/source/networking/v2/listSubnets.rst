
List subnets
============

.. rest_method::  GET /v2.0/subnets

Lists subnets to which the tenant has access.

Default policy settings returns exclusively subnets owned by the
tenant submitting the request, unless the request is submitted by a
user with administrative rights. You can control which attributes
are returned by using the fields query parameter. You can filter
results by using query string parameters.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml







Response Example
----------------

.. literalinclude:: ../samples/subnets/subnets-list-response.json
   :language: javascript




