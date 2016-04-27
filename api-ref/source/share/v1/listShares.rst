
List shares
===========

.. rest_method::  GET /v2/{tenant_id}/shares

Lists all shares.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - is_public: is_public
   - tenant_id: tenant_id
   - all_tenants: all_tenants
   - name: name
   - status: status
   - share_server_id: share_server_id
   - metadata: metadata
   - extra_specs: extra_specs
   - share_type_id: share_type_id
   - limit: limit
   - offset: offset
   - sort_key: sort_key
   - sort_dir: sort_dir
   - snapshot_id: snapshot_id
   - host: host
   - share_network_id: share_network_id
   - project_id: project_id
   - consistency_group_id: consistency_group_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-shares-list-response.json
   :language: javascript



