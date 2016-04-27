
Show cell capacities
====================

.. rest_method::  GET /v2.1/{tenant_id}/os-cells/{cell_id}/capacities

Shows capacities for a cell.

When cells are not enabled, the call returns the ``Not Implemented
(501)`` response code.


Normal response codes: 200
Error response codes:501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - cell_id: cell_id






Response Example
----------------

.. literalinclude:: ../samples/os-cells/cells-capacities-show-response.json
   :language: javascript




