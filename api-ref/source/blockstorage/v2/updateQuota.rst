
Update quotas
=============

.. rest_method::  PUT /v2/{admin_tenant_id}/os-quota-sets/{tenant_id}

Updates quotas for a tenant.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - injected_file_content_bytes: injected_file_content_bytes
   - metadata_items: metadata_items
   - reserved: reserved
   - in_use: in_use
   - ram: ram
   - floating_ips: floating_ips
   - key_pairs: key_pairs
   - injected_file_path_bytes: injected_file_path_bytes
   - instances: instances
   - security_group_rules: security_group_rules
   - injected_files: injected_files
   - quota_set: quota_set
   - cores: cores
   - fixed_ips: fixed_ips
   - id: id
   - security_groups: security_groups
   - tenant_id: tenant_id
   - admin_tenant_id: admin_tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-quota-sets/quotas-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - injected_file_content_bytes: injected_file_content_bytes
   - metadata_items: metadata_items
   - reserved: reserved
   - in_use: in_use
   - ram: ram
   - floating_ips: floating_ips
   - key_pairs: key_pairs
   - injected_file_path_bytes: injected_file_path_bytes
   - instances: instances
   - security_group_rules: security_group_rules
   - injected_files: injected_files
   - quota_set: quota_set
   - cores: cores
   - fixed_ips: fixed_ips
   - id: id
   - security_groups: security_groups




Response Example
----------------

.. literalinclude:: ../samples/os-quota-sets/quotas-update-response.json
   :language: javascript



