
Create credential
=================

.. rest_method::  POST /v3/credentials

Creates a credential.

The following example shows how to create an EC2-style credential.
The credential blob is a string that contains a JSON-serialized
dictionary with the ``access`` and ``secret`` keys. This format is
required when you specify the ``ec2`` type. To specify other
credentials, such as ``access_key``, change the type and contents
of the data blob.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - credential: credential
   - project_id: project_id
   - type: type
   - blob: blob
   - user_id: user_id

Request Example
---------------

.. literalinclude:: ../samples/admin/credential-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - credential: credential
   - user_id: user_id
   - links: links
   - blob: blob
   - project_id: project_id
   - type: type
   - id: id














