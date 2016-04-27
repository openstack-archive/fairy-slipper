
List users in group
===================

.. rest_method::  GET /v3/groups/{group_id}/users

Lists the users that belong to a group.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - group_id: group_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - links: links
   - enabled: enabled
   - domain_id: domain_id
   - email: email
   - id: id
   - users: users




Response Example
----------------

.. literalinclude:: ../samples/admin/group-users-list-response.json
   :language: javascript










