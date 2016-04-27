
List policies
=============

.. rest_method::  GET /v1/clusters/{cluster_id}/policies

Lists all policies for a cluster.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - cluster_id: cluster_id
   - sort: sort
   - enabled: enabled






Response Example
----------------

.. literalinclude:: ../samples/cluster-policies-list-response.json
   :language: javascript



