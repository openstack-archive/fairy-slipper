
Create snapshot
===============

.. rest_method::  POST /v2.1/{tenant_id}/os-snapshots

Creates a snapshot.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - snapshot: snapshot
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-volumes/snapshot-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-volumes/snapshot-show-response.json
   :language: javascript









