
List meters
===========

.. rest_method::  GET /v2/meters

Lists meters, based on the data recorded so far.


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
   - name: name
   - resource_id: resource_id
   - source: source
   - meter_id: meter_id
   - project_id: project_id
   - type: type
   - unit: unit




Response Example
----------------

.. literalinclude:: ../samples/meters-list-response.json
   :language: javascript



