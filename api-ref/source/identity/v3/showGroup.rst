
Show group details
==================

.. rest_method::  GET /v3/groups/{group_id}

Shows details for a group.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - group: group
   - name: name
   - links: links
   - domain_id: domain_id
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/group-show-response.json
   :language: javascript










