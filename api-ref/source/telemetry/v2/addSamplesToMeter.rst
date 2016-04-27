
Add samples to meter
====================

.. rest_method::  POST /v2/meters/{meter_name}

Adds samples to a meter, by meter name.

If you attempt to add a sample that is not supported, this call
returns the ``409`` response code.


Normal response codes: 200
Error response codes:409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - resource_id: resource_id
   - timestamp: timestamp
   - meter: meter
   - volume: volume
   - source: source
   - recorded_at: recorded_at
   - project_id: project_id
   - type: type
   - id: id
   - unit: unit
   - metadata: metadata
   - meter_name: meter_name
   - direct: direct
   - samples: samples

Request Example
---------------

.. literalinclude:: ../samples/sample-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - resource_id: resource_id
   - timestamp: timestamp
   - meter: meter
   - volume: volume
   - source: source
   - recorded_at: recorded_at
   - project_id: project_id
   - type: type
   - id: id
   - unit: unit
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/sample-show-response.json
   :language: javascript




