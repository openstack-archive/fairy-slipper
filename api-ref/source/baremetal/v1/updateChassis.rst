
Update chassis
==============

.. rest_method::  PATCH /v1/chassis/{chassis_id}

Updates a chassis.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - chassis: chassis
   - description: description
   - extra: extra

Request Example
---------------

.. literalinclude:: samples/chassis-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - links: links
   - extra: extra
   - created_at: created_at
   - updated_at: updated_at
   - chassis: chassis
   - nodes: nodes
   - uuid: uuid




Response Example
----------------

.. literalinclude:: samples/chassis-show-response.json
   :language: javascript












