
Create consistency group snapshot
=================================

.. rest_method::  POST /v2/{tenant_id}/cgsnapshots

Creates a consistency group snapshot.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/cgsnapshots/cgsnapshots-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - created_at: created_at
   - consistencygroup_id: consistencygroup_id
   - id: id
   - name: name





