
Scale cluster
=============

.. rest_method::  PUT /v1.1/{tenant_id}/clusters/{cluster_id}

Scales a cluster.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - cluster_id: cluster_id

Request Example
---------------

.. literalinclude:: ../samples/clusters/cluster-scale-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - count: count
   - info: info
   - cluster_template_id: cluster_template_id
   - is_transient: is_transient
   - provision_progress: provision_progress
   - status: status
   - neutron_management_network: neutron_management_network
   - management_public_key: management_public_key
   - status_description: status_description
   - trust_id: trust_id





