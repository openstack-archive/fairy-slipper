
Create chassis
==============

.. rest_method::  POST /v1/chassis

Creates a chassis.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - chassis: chassis
   - description: description
   - extra: extra

Request Example
---------------

.. literalinclude:: samples/chassis-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - extra: extra
   - created_at: created_at
   - updated_at: updated_at
   - nodes: nodes
   - uuid: uuid














