
Check token
===========

.. rest_method::  HEAD /v3/auth/tokens

Validates a token.

This call is similar to ``GET /auth/tokens`` but no response body
is provided even in the ``X-Subject-Token`` header.

The Identity API returns the same response as when the subject
token was issued by ``POST /auth/tokens`` even if an error occurs
because the token is not valid. An HTTP ``204`` response code
indicates that the ``X-Subject-Token`` is valid.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - X-Auth-Token: X-Auth-Token
   - X-Subject-Token: X-Subject-Token






Response Example
----------------

.. literalinclude:: 
   :language: javascript










