
Show sample details
===================

.. rest_method::  GET /v2/samples/{sample_id}

Shows details for a sample, by sample ID.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - sample_id: sample_id



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



