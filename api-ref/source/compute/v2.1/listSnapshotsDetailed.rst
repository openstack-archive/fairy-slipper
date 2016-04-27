
List snapshots with details
===========================

.. rest_method::  GET /v2.1/{tenant_id}/os-snapshots/detail

Lists all snapshots with details.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-volumes/snapshots-list-response.json
   :language: javascript









