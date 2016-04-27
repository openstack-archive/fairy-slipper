
Show chassis details
====================

.. rest_method::  GET /v1/chassis/{chassis_id}

Shows details for a chassis.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - fields: fields



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - uuid: uuid
   - chassis: chassis
   - description: description
   - extra: extra




Response Example
----------------

.. literalinclude:: samples/chassis-show-response.json
   :language: javascript










