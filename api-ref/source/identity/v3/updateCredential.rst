
Update credential
=================

.. rest_method::  PATCH /v3/credentials/{credential_id}

Updates a credential.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - credential: credential
   - project_id: project_id
   - type: type
   - blob: blob
   - user_id: user_id
   - credential_id: credential_id

Request Example
---------------

.. literalinclude:: ../samples/admin/credential-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - credential: credential
   - user_id: user_id
   - links: links
   - blob: blob
   - project_id: project_id
   - type: type
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/credential-update-response.json
   :language: javascript












