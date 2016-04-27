
Update port
===========

.. rest_method::  PUT /v2.0/ports/{port_id}

Updates a port.


Normal response codes: 200
Error response codes:404,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - port_id: port_id

Request Example
---------------

.. literalinclude:: ../samples/ports/port-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/ports/port-bind-create-update-response.json
   :language: javascript






