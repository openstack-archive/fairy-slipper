
List cells
==========

.. rest_method::  GET /v2.1/{tenant_id}/os-cells

Lists cells.

When cells are not enabled, the call returns the ``Not Implemented
(501)`` response code.


Normal response codes: 200
Error response codes:501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-cells/cells-list-response.json
   :language: javascript




