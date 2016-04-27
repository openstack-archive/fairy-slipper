
List groups
===========

.. rest_method::  GET /v3/groups

Lists groups.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - links: links
   - domain_id: domain_id
   - groups: groups
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/groups-list-response.json
   :language: javascript










