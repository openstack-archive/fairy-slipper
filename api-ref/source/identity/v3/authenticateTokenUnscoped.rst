
Token authentication with unscoped authorization
================================================

.. rest_method::  POST /v3/auth/tokens

Authenticates an identity and generates a token. Uses the token authentication method. Authorization is unscoped.

In the request body, provide the token ID.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - identity: identity
   - token: token
   - id: id
   - auth: auth
   - methods: methods
   - nocatalog: nocatalog

Request Example
---------------

.. literalinclude:: ../samples/admin/auth-token-unscoped-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Subject-Token: X-Subject-Token
   - X-Auth-Token: X-Auth-Token














