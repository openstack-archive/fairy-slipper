
Show metering label details
===========================

.. rest_method::  GET /v2.0/metering/metering-labels/{metering-label-id}

Shows details for a metering label.

The response body shows the description, name, and UUID.


Normal response codes: 200
Error response codes:404,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - metering_label: metering_label
   - shared: shared
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/metering-labels/metering-label-show-response.json
   :language: javascript





