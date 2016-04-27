
Show port interface details
===========================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-interface/{port_id}

Shows details for a port interface that is attached to a server.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - port_id: port_id






Response Example
----------------

.. literalinclude:: ../samples/os-interface/port-interface-show-response.json
   :language: javascript









