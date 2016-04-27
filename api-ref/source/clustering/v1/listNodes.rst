
List nodes
==========

.. rest_method::  GET /v1/nodes

Lists all nodes.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - limit: limit
   - marker: marker
   - sort: sort
   - global_project: global_project
   - cluster_id: cluster_id
   - name: name
   - status: status



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - nodes: nodes




Response Example
----------------

.. literalinclude:: ../samples/nodes-list-response.json
   :language: javascript



