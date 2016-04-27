
Update group
============

.. rest_method::  PATCH /v3/groups/{group_id}

Updates a group.

If the back-end driver does not support this functionality, the
call returns the ``Not Implemented (501)`` response code.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group: group
   - description: description
   - name: name
   - domain_id: domain_id
   - group_id: group_id

Request Example
---------------

.. literalinclude:: ../samples/admin/group-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/admin/group-update-response.json
   :language: javascript












