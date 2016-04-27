
List available clusters
=======================

.. rest_method::  GET /v1.1/{tenant_id}/clusters

Lists available clusters.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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
   - clusters: clusters
   - management_public_key: management_public_key
   - status_description: status_description
   - trust_id: trust_id




Response Example
----------------

.. literalinclude:: ../samples/clusters/clusters-list-response.json
   :language: javascript



