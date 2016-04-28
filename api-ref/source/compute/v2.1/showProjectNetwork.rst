
Show project network details
============================

.. rest_method::  GET /v2.1/{tenant_id}/os-tenant-networks/{network_id}

Shows details for a project network.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - network_id: network_id
   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-tenant-networks/network-show-response.json
   :language: javascript



