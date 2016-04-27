
Create share network
====================

.. rest_method::  POST /v2/{tenant_id}/share-networks

Creates a share network.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - nova_net_id: nova_net_id
   - neutron_net_id: neutron_net_id
   - neutron_subnet_id: neutron_subnet_id
   - description: description
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-network-create-request.json
   :language: javascript




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

.. literalinclude:: ../samples/manila-share-network-create-response.json
   :language: javascript



