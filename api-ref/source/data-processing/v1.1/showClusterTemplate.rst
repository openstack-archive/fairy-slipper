
Show cluster template details
=============================

.. rest_method::  GET /v1.1/{tenant_id}/cluster-templates/{cluster_template_id}

Shows details for a cluster template.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - cluster_template_id: cluster_template_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - use_autoconfig: use_autoconfig
   - cluster_configs: cluster_configs
   - created_at: created_at
   - default_image_id: default_image_id
   - updated_at: updated_at
   - plugin_name: plugin_name
   - is_default: is_default
   - is_protected: is_protected
   - shares: shares
   - tenant_id: tenant_id
   - node_groups: node_groups
   - is_public: is_public
   - hadoop_version: hadoop_version
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/cluster-templates/cluster-templates-list-response.json
   :language: javascript



