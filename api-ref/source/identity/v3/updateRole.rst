
Update role
===========

.. rest_method::  PATCH /v3/roles/{role_id}

Updates a role.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role: role
   - name: name
   - role_id: role_id

Request Example
---------------

.. literalinclude:: ../samples/admin/role-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - role: role
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/role-update-response.json
   :language: javascript












