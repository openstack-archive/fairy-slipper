
List flavors
============

.. rest_method::  GET /v1.0/{accountId}/flavors

Lists information for all available flavors.

This operation lists information for all available flavors.

This resource is identical to the flavors found in the OpenStack
Nova API, but without the disk property.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-flavors-response.json
   :language: javascript













