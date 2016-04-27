
List consistency group snapshots
================================

.. rest_method::  GET /v2/{tenant_id}/cgsnapshots

Lists all consistency group snapshots.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - link: link
   - id: id
   - cgsnapshots: cgsnapshots
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-cg-snapshots-list-response.json
   :language: javascript



