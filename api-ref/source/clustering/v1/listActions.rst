
List actions
============

.. rest_method::  GET /v1/actions

Lists all actions.


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
   - target: target
   - action: action






Response Example
----------------

.. literalinclude:: ../samples/actions-list-response.json
   :language: javascript



