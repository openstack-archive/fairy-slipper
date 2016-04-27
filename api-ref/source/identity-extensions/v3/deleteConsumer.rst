
Delete consumer
===============

.. rest_method::  DELETE /v3/OS-OAUTH1/consumers/{consumer_id}

Deletes a consumer.

When you delete a consumer, any associated request tokens, access
tokens, and Identity API tokens are also deleted.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - consumer_id: consumer_id
















