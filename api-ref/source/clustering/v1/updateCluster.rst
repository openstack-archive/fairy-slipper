
Update cluster
==============

.. rest_method::  PATCH /v1/clusters/{cluster_id}

Updates a cluster.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - parent: parent
   - profile_id: profile_id
   - cluster: cluster
   - timeout: timeout
   - metadata: metadata
   - cluster_id: cluster_id

Request Example
---------------

.. literalinclude:: ../samples/cluster-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - location: location
   - cluster: cluster





