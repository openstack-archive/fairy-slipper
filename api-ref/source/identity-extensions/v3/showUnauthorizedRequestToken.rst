
Show unauthorized request token
===============================

.. rest_method::  POST /v3/OS-OAUTH1/request_token

Enables a consumer to get an unauthorized request token.

Supported signature methods: HMAC-SHA1.

The consumer must provide all required OAuth parameters in the
request. See `Consumer Obtains a Request Token
<http://oauth.net/core/1.0a/#auth_step1>`_.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml







Response Example
----------------

.. literalinclude:: ../samples/OS-OAUTH1/request-token-create-response.txt
   :language: javascript












