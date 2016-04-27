
Update consumer
===============

.. rest_method::  PATCH /v3/OS-OAUTH1/consumers/{consumer_id}

Updates the description for a consumer.

If you try to update any attribute other than description, the HTTP
400 Bad Request error is returned.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - consumer_id: consumer_id

Request Example
---------------

.. literalinclude:: ../samples/OS-OAUTH1/consumer-update-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/OS-OAUTH1/consumer-update-response.json
   :language: javascript












