
Show security group details
===========================

.. rest_method::  GET /v2.1/{tenant_id}/os-security-groups/{security_group_id}

Shows details for a security group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - security_group_id: security_group_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - rules: rules
   - tenant_id: tenant_id
   - security_group: security_group
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/os-security-groups/security-group-show-response.json
   :language: javascript



