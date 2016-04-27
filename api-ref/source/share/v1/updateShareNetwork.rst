
Update share network
====================

.. rest_method::  PUT /v2/{tenant_id}/share-networks/{share_network_id}

Updates a share network.

Note that if the share network is used by any share server, you can
update only the ``name`` and ``description`` attributes.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - name: name
   - tenant_id: tenant_id
   - share_network_id: share_network_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-network-update-request.json
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

.. literalinclude:: ../samples/manila-share-network-update-response.json
   :language: javascript



