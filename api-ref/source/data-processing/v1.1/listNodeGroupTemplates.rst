
List node group templates
=========================

.. rest_method::  GET /v1.1/{tenant_id}/node-group-templates

Lists available node group templates.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - volume_local_to_instance: volume_local_to_instance
   - availability_zone: availability_zone
   - updated_at: updated_at
   - use_autoconfig: use_autoconfig
   - volumes_per_node: volumes_per_node
   - id: id
   - security_groups: security_groups
   - shares: shares
   - node_configs: node_configs
   - auto_security_group: auto_security_group
   - volumes_availability_zone: volumes_availability_zone
   - description: description
   - volume_mount_prefix: volume_mount_prefix
   - plugin_name: plugin_name
   - floating_ip_pool: floating_ip_pool
   - is_default: is_default
   - image_id: image_id
   - volumes_size: volumes_size
   - is_proxy_gateway: is_proxy_gateway
   - is_public: is_public
   - hadoop_version: hadoop_version
   - name: name
   - tenant_id: tenant_id
   - created_at: created_at
   - volume_type: volume_type
   - is_protected: is_protected
   - node_processes: node_processes
   - flavor_id: flavor_id




Response Example
----------------

.. literalinclude:: ../samples/node-group-templates/node-group-templates-list-response.json
   :language: javascript



