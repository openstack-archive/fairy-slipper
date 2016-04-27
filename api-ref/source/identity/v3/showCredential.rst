
Show credential details
=======================

.. rest_method::  GET /v3/credentials/{credential_id}

Shows details for a credential.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - credential_id: credential_id



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

.. literalinclude:: ../samples/admin/credential-show-response.json
   :language: javascript










