
Validate token
==============

.. rest_method::  GET /v2.0/tokens/{tokenId}

Validates a token and confirms that it belongs to a tenant.

Returns the permissions relevant to a particular client. Valid
tokens are in the ``/tokens/{tokenId}`` path. If the token is not
valid, this call returns the ``itemNotFound (404)`` response code.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tokenId: tokenId






Response Example
----------------

.. literalinclude:: ../samples/admin/token-validate-response.json
   :language: javascript











