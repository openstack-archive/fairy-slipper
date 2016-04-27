
Get an Identity Service token
=============================

.. rest_method::  POST /v3/auth/tokens

Enables a consumer to get an Identity Service authentication token.

The token represents the delegated authorization and identity
(impersonation) of the authorizing user. The roles and scope of the
generated token match those that the consumer initially requested.

Supported signature methods: HMAC-SHA1.

The consumer must provide required OAuth parameters in the request.
See `Consumer Obtains a Request Token
<http://oauth.net/core/1.0a/#auth_step1>`_.

The returned token is scoped to the requested project and with the
requested roles. In addition to the standard token response, the
token has an OAuth-specific object.

Example OAuth-specific object in a token:

.. code-block:: json

   "OS-OAUTH1": {
       "access_token_id": "cce0b8be7"
   }


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml







Response Example
----------------

.. literalinclude:: 
   :language: javascript










