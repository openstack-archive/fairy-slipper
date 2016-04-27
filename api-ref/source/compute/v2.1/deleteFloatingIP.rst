
Delete (deallocate) floating IP address
=======================================

.. rest_method::  DELETE /v2.1/{tenant_id}/os-floating-ips/{floating_ip_id}

Deletes, or deallocates, a floating IP address from the current project and returns it to the pool from which it was allocated.

If the IP address is still associated with a running instance, it
is automatically disassociated from that instance.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - floating_ip_id: floating_ip_id
   - tenant_id: tenant_id







