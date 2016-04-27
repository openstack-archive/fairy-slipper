
Get authorized access token
===========================

.. rest_method::  GET /v3/OS-OAUTH1/users/{user_id}/access_tokens/{access_token_id}

Gets an authorized access token.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - access_token_id: access_token_id






Response Example
----------------

.. literalinclude:: ../samples/OS-OAUTH1/access-token-show-response.json
   :language: javascript










