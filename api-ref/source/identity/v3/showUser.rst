
Show user details
=================

.. rest_method::  GET /v3/users/{user_id}

Shows details for a user.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - user: user
   - enabled: enabled
   - email: email
   - default_project_id: default_project_id
   - id: id
   - domain_id: domain_id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/user-show-response.json
   :language: javascript










