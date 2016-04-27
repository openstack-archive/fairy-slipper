
Create project network
======================

.. rest_method::  POST /v2.1/{tenant_id}/os-tenant-networks

Creates a project network.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-tenant-networks/network-create-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-tenant-networks/network-create-response.json
   :language: javascript



