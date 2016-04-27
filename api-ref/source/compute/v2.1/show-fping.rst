
Ping an instance
================

.. rest_method::  GET /v2.1/{tenant_id}/os-fping/{instance_id}

Run the fping utility to ping an instance and report whether it is alive.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instance_id: instance_id
   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-fping/fping-instance-show-response.json
   :language: javascript



