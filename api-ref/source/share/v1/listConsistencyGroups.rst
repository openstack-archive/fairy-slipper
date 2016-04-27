
List consistency groups
=======================

.. rest_method::  GET /v2/{tenant_id}/consistency-groups

Lists all consistency groups.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - consistency_groups: consistency_groups
   - link: link
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-consistency-groups-list-response.json
   :language: javascript



