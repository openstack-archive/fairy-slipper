
Get SPICE console (os-getSPICEConsole action)
=============================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Gets a SPICE console for a server.

Specify the ``os-getSPICEConsole`` action in the request body.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - os-getSPICEConsole: os-getSPICEConsole
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/getSPICEConsole-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/servers-action/getSPICEConsole-create-response.json
   :language: javascript



