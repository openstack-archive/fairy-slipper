
List samples
============

.. rest_method::  GET /v2/samples

Lists all known samples, based on the data recorded so far.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - q: q
   - limit: limit



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

.. literalinclude:: ../samples/samples-list-response.json
   :language: javascript



