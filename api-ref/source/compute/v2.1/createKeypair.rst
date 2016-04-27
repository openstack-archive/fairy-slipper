
Create or import keypair
========================

.. rest_method::  POST /v2.1/{tenant_id}/os-keypairs

Generates or imports a keypair.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - public_key: public_key
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-keypairs/keypair-import-request.json
   :language: javascript







Response Example
----------------

.. literalinclude:: ../samples/os-keypairs/keypair-import-response.json
   :language: javascript



