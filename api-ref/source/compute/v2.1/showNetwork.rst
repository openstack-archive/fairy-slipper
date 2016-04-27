
Show network details
====================

.. rest_method::  GET /v2.1/{tenant_id}/os-networks/{network_id}

Shows details for a network.

Policy defaults enable all users to perform this operation. Cloud
providers can change these permissions through the ``policy.json``
file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - network_id: network_id
   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-networks/network-show-response.json
   :language: javascript



