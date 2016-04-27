
List metering labels
====================

.. rest_method::  GET /v2.0/metering/metering-labels

Lists all L3 metering labels that belong to the tenant.

The list shows the UUID for each metering label.


Normal response codes: 200
Error response codes:401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - metering_labels: metering_labels
   - shared: shared
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/metering-labels/metering-labels-list-response.json
   :language: javascript




