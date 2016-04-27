
Create access token
===================

.. rest_method::  POST /v3/OS-OAUTH1/access_token

Enables a consumer to create an access token by exchanging a request token for an access token.

After the user authorizes the request token, the consumer exchanges
the authorized request token and OAuth verifier for an access
token.

Supported signature methods: HMAC-SHA1.

The consumer must provide all required OAuth parameters in the
request. See `Consumer Obtains a Request Token
<http://oauth.net/core/1.0a/#auth_step1>`_.

Supported signature methods: HMAC-SHA1.

You must provide all required OAuth parameters in the request. See
`Consumer Obtains a Request Token
<http://oauth.net/core/1.0a/#auth_step1>`_.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml







Response Example
----------------

.. literalinclude:: ../samples/OS-OAUTH1/access-token-create-response.txt
   :language: javascript












