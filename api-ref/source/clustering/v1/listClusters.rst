
List clusters
=============

.. rest_method::  GET /v1/clusters

Lists clusters.


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
   - status: status



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - clusters: clusters




Response Example
----------------

.. literalinclude:: ../samples/clusters-list-response.json
   :language: javascript



