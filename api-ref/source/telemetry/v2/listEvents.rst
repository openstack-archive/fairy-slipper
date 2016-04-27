
List events
===========

.. rest_method::  GET /v2/events

Lists all events.


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

   - traits: traits
   - raw: raw
   - generated: generated
   - event_type: event_type
   - message_id: message_id




Response Example
----------------

.. literalinclude:: ../samples/events-list-response.json
   :language: javascript



