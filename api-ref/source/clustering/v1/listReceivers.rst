
List receivers
==============

.. rest_method::  GET /v1/receivers

Lists all receivers.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort: sort
   - global_project: global_project
   - name: name
   - type: type
   - user: user
   - cluster_id: cluster_id
   - action: action






Response Example
----------------

.. literalinclude:: ../samples/receivers-list-response.json
   :language: javascript



