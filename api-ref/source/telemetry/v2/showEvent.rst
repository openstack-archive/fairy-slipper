
Show event details
==================

.. rest_method::  GET /v2/events/{message_id}

Shows details for an event.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - message_id: message_id



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

.. literalinclude:: ../samples/event-show-response.json
   :language: javascript



