
Validate token (admin)
======================

.. rest_method::  HEAD /v2.0/tokens/{tokenId}

Validates a token and confirms that it belongs to a tenant, for performance.


Normal response codes: 200
Error response codes:203,204,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tokenId: tokenId






Response Example
----------------

.. literalinclude:: 
   :language: javascript












