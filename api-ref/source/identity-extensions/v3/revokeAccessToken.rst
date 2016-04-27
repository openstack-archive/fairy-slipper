
Revoke access token
===================

.. rest_method::  DELETE /v3/OS-OAUTH1/users/{user_id}/access_tokens/{access_token_id}

Enables a user to revoke an access token, which prevents the consumer from requesting new Identity Service API tokens. Also, revokes any Identity Service API tokens that were issued to the consumer through that access token.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - access_token_id: access_token_id
















