
Show cell data
==============

.. rest_method::  GET /v2.1/{tenant_id}/os-cells/{cell_id}

Shows data for a cell.

When cells are not enabled, the call returns the ``Not Implemented
(501)`` response code.


Normal response codes: 200
Error response codes:501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - cell_id: cell_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-cells/cell-show-response.json
   :language: javascript




