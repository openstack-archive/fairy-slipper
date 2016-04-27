
Show driver properties
======================

.. rest_method::  GET /v1/drivers/{driver_name}/properties

Shows properties for a driver.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - driver_name: driver_name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - hosts: hosts
   - name: name
   - links: links
   - properties: properties




Response Example
----------------

.. literalinclude:: samples/driver-get-response.json
   :language: javascript










