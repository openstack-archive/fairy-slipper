
List credentials
================

.. rest_method::  GET /v3/credentials

Lists all credentials.

Optionally, you can include the ``user_id`` query parameter in the
URI to filter the response by a user.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - links: links
   - blob: blob
   - credentials: credentials
   - project_id: project_id
   - type: type
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/credentials-list-response.json
   :language: javascript










