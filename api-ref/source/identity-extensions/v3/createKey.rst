
Create key
==========

.. rest_method::  POST /v3/keys/{name}

Creates a long-term key in the KDS.

The request body contains the key.

The response shows the key name and generation value.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name

Request Example
---------------

.. literalinclude:: ../samples/OS-KDS/key-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - generation: generation
   - name: name














