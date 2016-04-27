
Run events
==========

.. rest_method::  POST /v2.1/{tenant_id}/os-server-external-events

Creates one or more external events, which the API dispatches to the instance.

You must assign this instance to a host. Otherwise, this call does
not dispatch the event to the instance.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - tag: tag
   - events: events
   - server_uuid: server_uuid
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-server-external-events/event-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - code: code
   - name: name
   - tag: tag
   - server_uuid: server_uuid
   - events: events




Response Example
----------------

.. literalinclude:: ../samples/os-server-external-events/event-create-response.json
   :language: javascript



