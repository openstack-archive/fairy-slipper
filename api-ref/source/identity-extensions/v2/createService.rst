
Create service
==============

.. rest_method::  POST /v2.0/services

Creates a service.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/OS-KSADM/service-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Location: Location
   - type: type
   - description: description
   - name: name
   - id: id














