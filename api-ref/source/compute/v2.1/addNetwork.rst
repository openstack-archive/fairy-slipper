
Add network
===========

.. rest_method::  POST /v2.1/{tenant_id}/os-networks/add

Adds a network to a project.

Policy defaults enable only users with the administrative role to
perform this operation. Cloud providers can change these
permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-networks/network-add-request.json
   :language: javascript








