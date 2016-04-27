
Create node
===========

.. rest_method::  POST /v1/nodes

Creates a node.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - role: role
   - profile_id: profile_id
   - cluster_id: cluster_id
   - name: name
   - metadata: metadata

Request Example
---------------

.. literalinclude:: ../samples/node-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - location: location
   - node: node





