
Show share network details
==========================

.. rest_method::  GET /v2/{tenant_id}/share-networks/{share_network_id}

Shows details for a share network.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - share_network_id: share_network_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - neutron_net_id: neutron_net_id
   - created_at: created_at
   - neutron_subnet_id: neutron_subnet_id
   - updated_at: updated_at
   - network_type: network_type
   - segmentation_id: segmentation_id
   - ip_version: ip_version
   - nova_net_id: nova_net_id
   - cidr: cidr
   - project_id: project_id
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/manila-share-network-show-response.json
   :language: javascript



