
Create metering label
=====================

.. rest_method::  POST /v2.0/metering/metering-labels

Creates an L3 metering label.

Error response codes:201,403,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - shared: shared
   - metering_label: metering_label
   - description: description
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/metering-labels/metering-label-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - metering_label: metering_label
   - shared: shared
   - id: id
   - name: name








