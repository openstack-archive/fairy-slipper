
Show role details
=================

.. rest_method::  GET /v3/roles/{role_id}

Shows details for a role.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role_id: role_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - role: role
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/role-show-response.json
   :language: javascript










