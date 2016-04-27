
Shows service information by ID
===============================

.. rest_method::  GET /v2.0/services/{serviceId}

Shows information for a service, by ID.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - serviceId: serviceId



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - type: type
   - description: description
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/OS-KSADM/service-show-response.json
   :language: javascript











