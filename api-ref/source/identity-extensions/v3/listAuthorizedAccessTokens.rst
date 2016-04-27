
List authorized access tokens
=============================

.. rest_method::  GET /v3/OS-OAUTH1/users/{user_id}/access_tokens

Lists authorized access tokens.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id






Response Example
----------------

.. literalinclude:: ../samples/OS-OAUTH1/access-tokens-list-response.json
   :language: javascript










