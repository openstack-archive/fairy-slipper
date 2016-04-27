
Add (associate) floating IP (addFloatingIp action)
==================================================

.. rest_method::  POST /v2.1/{tenant_id}/servers/{server_id}/action

Adds a floating IP address to a server, which associates that address with the server.

A pool of floating IP addresses, configured by the cloud
administrator, is available in OpenStack Compute. The project quota
defines the maximum number of floating IP addresses that you can
allocate to the project. After you `create (allocate) a floating IP
address <http://developer.openstack.org/api-ref-
compute-v2.1.html#createFloatingIP>`_ for a project, you can
associate that address with the server. Specify the
``addFloatingIp`` action in the request body.

If an instance is connected to multiple networks, you can associate
a floating IP address with a specific fixed IP address by using the
optional ``fixed_address`` parameter.

Preconditions

- The server must exist.

- You can only add a floating IP address to the server when its
  status is ``available``.

Error response codes:202,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - fixed_address: fixed_address
   - addFloatingIp: addFloatingIp
   - address: address
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers-action/addFloatingIp-request.json
   :language: javascript
















