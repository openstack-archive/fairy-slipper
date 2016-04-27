
Create group
============

.. rest_method::  POST /v3/groups

Creates a group.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group: group
   - description: description
   - name: name
   - domain_id: domain_id

Request Example
---------------

.. literalinclude:: ../samples/admin/group-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - group: group
   - name: name
   - links: links
   - domain_id: domain_id
   - id: id
   - description: description














