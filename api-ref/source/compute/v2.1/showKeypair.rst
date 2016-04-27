
Show keypair details
====================

.. rest_method::  GET /v2.1/{tenant_id}/os-keypairs/{keypair_name}

Shows details for a keypair that is associated with the account.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - keypair_name: keypair_name






Response Example
----------------

.. literalinclude:: ../samples/os-keypairs/keypair-show-response.json
   :language: javascript



