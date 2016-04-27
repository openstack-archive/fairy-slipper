
Remove security service from share network
==========================================

.. rest_method::  POST /v2/{tenant_id}/share-networks/{share_network_id}/action

Removes a security service from a share network.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - security_service_id: security_service_id
   - tenant_id: tenant_id
   - share_network_id: share_network_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-network-remove-security-service-request.json
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

.. literalinclude:: ../samples/manila-share-network-remove-security-service-response.json
   :language: javascript



