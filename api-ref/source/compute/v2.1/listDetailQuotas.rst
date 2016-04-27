
List quotas with details
========================

.. rest_method::  GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}/detail

Lists quotas with details for a project or a project and a user.

To list a quota for a project and a user, specify the ``user_id``
query parameter.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - admin_tenant_id: admin_tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - injected_file_content_bytes: injected_file_content_bytes
   - metadata_items: metadata_items
   - reserved: reserved
   - server_group_members: server_group_members
   - in_use: in_use
   - ram: ram
   - floating_ips: floating_ips
   - key_pairs: key_pairs
   - injected_file_path_bytes: injected_file_path_bytes
   - server_groups: server_groups
   - instances: instances
   - limit: limit
   - security_group_rules: security_group_rules
   - injected_files: injected_files
   - quota_set: quota_set
   - cores: cores
   - fixed_ips: fixed_ips
   - id: id
   - security_groups: security_groups




Response Example
----------------

.. literalinclude:: ../samples/os-quota-sets/quotas-list-details-response.json
   :language: javascript



