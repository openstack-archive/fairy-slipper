
List default quotas for tenant
==============================

.. rest_method::  GET /v2.1/{admin_tenant_id}/os-quota-sets/{tenant_id}/defaults

Lists the default quotas for a project.

In the request URI, you specify both the ID of the administrative
project and the ID of the project for which you want to show
default quotas. These project IDs can match.


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

   - injected_file_content_bytes: injected_file_content_bytes
   - metadata_items: metadata_items
   - server_group_members: server_group_members
   - server_groups: server_groups
   - ram: ram
   - floating_ips: floating_ips
   - key_pairs: key_pairs
   - id: id
   - instances: instances
   - security_group_rules: security_group_rules
   - injected_files: injected_files
   - quota_set: quota_set
   - cores: cores
   - fixed_ips: fixed_ips
   - injected_file_path_bytes: injected_file_path_bytes
   - security_groups: security_groups




Response Example
----------------

.. literalinclude:: ../samples/os-quota-sets/quotas-default-list-response.json
   :language: javascript



