
List consistency group snapshots with details
=============================================

.. rest_method::  GET /v2/{tenant_id}/cgsnapshots/detail

Lists all consistency group snapshots with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - created_at: created_at
   - consistencygroup_id: consistencygroup_id
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/cgsnapshots/cgsnapshots-list-detailed-response.json
   :language: javascript



