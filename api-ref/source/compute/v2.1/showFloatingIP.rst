
Show floating IP address details
================================

.. rest_method::  GET /v2.1/{tenant_id}/os-floating-ips/{floating_ip_id}

Shows details for a floating IP address, by ID, that is associated with the tenant or account.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - floating_ip_id: floating_ip_id
   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: ../samples/os-floating-ips/floating-ip-show-response.json
   :language: javascript



