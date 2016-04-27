
List floating IP addresses
==========================

.. rest_method::  GET /v2.1/{tenant_id}/os-floating-ips

Lists floating IP addresses associated with the tenant or account.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-floating-ips/floating-ips-list-response.json
   :language: javascript



