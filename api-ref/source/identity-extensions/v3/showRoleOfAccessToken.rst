
Show role details for an access token
=====================================

.. rest_method::  GET /v3/OS-OAUTH1/users/{user_id}/access_tokens/{access_token_id}/roles/{role_id}

Shows details for a role for an access token.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - role_id: role_id
   - access_token_id: access_token_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript










