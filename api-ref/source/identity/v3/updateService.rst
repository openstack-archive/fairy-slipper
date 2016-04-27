
Update service
==============

.. rest_method::  PATCH /v3/services/{service_id}

Updates a service.

The request body is the same as the create service request body,
except that you include only those attributes that you want to
update.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - type: type
   - enabled: enabled
   - description: description
   - service: service
   - name: name
   - service_id: service_id

Request Example
---------------

.. literalinclude:: ../samples/admin/service-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - service: service
   - links: links
   - type: type
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/service-update-response.json
   :language: javascript












