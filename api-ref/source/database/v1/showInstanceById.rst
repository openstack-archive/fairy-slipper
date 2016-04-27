
Show database instance details
==============================

.. rest_method::  GET /v1.0/{accountId}/instances/{instanceId}

Shows database instance details.

Lists the status and details of the database instance.

Lists the volume size in gigabytes (GB) and the approximate GB
used.

After instance creation, the ``used`` value is greater than 0,
which is expected and due to the automatic creation of non-empty
transaction logs for MySQL optimization. The response does not
include the ``used`` attribute when the instance status is
``BUILD``, ``REBOOT``, ``RESIZE``, or ``ERROR``.

The list operations return a DNS-resolvable host name for the
database instance rather than an IP address. Because the host name
always resolves to the correct IP address for the database
instance, you do not need to maintain the mapping. Although the IP
address might change when you resize, migrate, or perform other
operations, the host name always resolves to the correct database
instance.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-instance-status-detail-response.json
   :language: javascript













