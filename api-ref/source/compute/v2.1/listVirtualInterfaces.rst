
List virtual interfaces
=======================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-virtual-interfaces

Lists the virtual interfaces for an instance.

Policy defaults enable only users with the administrative role or
the owner of the server to perform this operation. Change these
permissions through the ``policy.json`` file.

The API v2 returns the network ID in the ``OS-EXT-VIF-NET:net_id``
response attribute.

The API v2.1 base version does not return the network ID.

The API v2.12 microversion returns the network ID in the ``net_id``
response attribute.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - virtual_interfaces: virtual_interfaces
   - mac_address: mac_address




Response Example
----------------

.. literalinclude:: ../samples/os-virtual-interfaces/vifs-list-response.json
   :language: javascript









