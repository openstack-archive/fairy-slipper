
Create cluster
==============

.. rest_method::  POST /v1/clusters

Creates a cluster.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - parent: parent
   - desired_capacity: desired_capacity
   - profile_id: profile_id
   - min_size: min_size
   - cluster: cluster
   - timeout: timeout
   - max_size: max_size
   - metadata: metadata

Request Example
---------------

.. literalinclude:: ../samples/cluster-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - location: location
   - cluster: cluster





