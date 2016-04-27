
List drivers
============

.. rest_method::  GET /v1/drivers

Lists all drivers.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - drivers: drivers
   - hosts: hosts
   - name: name




Response Example
----------------

.. literalinclude:: samples/drivers-list-response.json
   :language: javascript










