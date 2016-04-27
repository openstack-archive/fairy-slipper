
Update quota
============

.. rest_method::  PUT /v2.1/{tenant_id}/os-quota-class-sets/{class_id}

Updates quota for a class.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - class_id: class_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-quota-class-sets/quota-class-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/os-quota-class-sets/quota-class-update-response.json
   :language: javascript



