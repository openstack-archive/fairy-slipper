
Revoke token
============

.. rest_method::  DELETE /v3/auth/tokens

Revokes a token.

This call is similar to the HEAD ``/auth/tokens`` call except that
the ``X-Subject-Token`` token is immediately not valid, regardless
of the ``expires_at`` attribute value. An additional ``X-Auth-
Token`` is not required.

Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - X-Auth-Token: X-Auth-Token
   - X-Subject-Token: X-Subject-Token















