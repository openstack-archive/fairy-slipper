
List events
===========

.. rest_method::  GET /v1/events

Lists events.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort: sort
   - global_project: global_project
   - obj_id: obj_id
   - obj_type: obj_type
   - obj_name: obj_name
   - cluster_id: cluster_id
   - action: action






Response Example
----------------

.. literalinclude:: ../samples/events-list-response.json
   :language: javascript



