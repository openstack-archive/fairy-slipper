
Disassociate host
=================

.. rest_method::  POST /v2.1/{tenant_id}/os-networks/{network_id}/action

Disassociates a host from a network.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - network_id: network_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-networks/network-disassociate-host-request.json
   :language: javascript








