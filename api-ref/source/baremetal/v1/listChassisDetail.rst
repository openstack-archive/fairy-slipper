
List chassis with details
=========================

.. rest_method::  GET /v1/chassis/detail

Lists all chassis with details.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort_dir: sort_dir
   - sort_key: sort_key



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - uuid: uuid
   - chassis: chassis
   - description: description
   - extra: extra




Response Example
----------------

.. literalinclude:: samples/chassis-list-details-response.json
   :language: javascript










