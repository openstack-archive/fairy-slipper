
Create role
===========

.. rest_method::  POST /v3/roles

Creates a role.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role: role
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/admin/role-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - role: role
   - id: id
   - links: links
   - name: name














