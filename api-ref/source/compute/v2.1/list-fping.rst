
Ping instances
==============

.. rest_method::  GET /v2.1/{tenant_id}/os-fping

Run the fping utility to ping instances and report which ones are alive.

Specify the ``all_tenants=1`` query parameter to ping instances for
all tenants. For example:

.. code-block:: json

   GET /os-fping?all_tenants=1

Specify the ``include`` and ``exclude`` query parameters to filter
the results. For example:

.. code-block:: json

   GET /os-fping?all_tenants=1
   &
   include=uuid1,uuid2
   &
   exclude=uuid3,uuid4

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Cloud providers
can change these permissions through the ``policy.json`` file.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - all_tenants: all_tenants
   - include: include
   - exclude: exclude






Response Example
----------------

.. literalinclude:: ../samples/os-fping/fping-instances-list-response.json
   :language: javascript



