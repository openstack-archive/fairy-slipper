
List users
==========

.. rest_method::  GET /v3/users

Lists users.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - name: name
   - enabled: enabled



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - enabled: enabled
   - email: email
   - default_project_id: default_project_id
   - id: id
   - users: users
   - domain_id: domain_id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/users-list-response.json
   :language: javascript










