
List networks
=============

.. rest_method::  GET /v2.1/{tenant_id}/os-networks

Lists networks for the project.

Policy defaults enable all users to perform this operation. Cloud
providers can change these permissions through the ``policy.json``
file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-networks/networks-list-response.json
   :language: javascript



