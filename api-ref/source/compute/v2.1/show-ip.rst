
Show IP details
===============

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/ips/{network_label}

Shows IP addresses details for a network label of a server instance.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - network_label: network_label






Response Example
----------------

.. literalinclude:: ../samples/ips/ips-network-response.json
   :language: javascript



