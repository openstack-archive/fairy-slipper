
Update security group
=====================

.. rest_method::  PUT /v2.1/{tenant_id}/os-security-groups/{security_group_id}

Updates a security group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - name: name
   - tenant_id: tenant_id
   - security_group_id: security_group_id

Request Example
---------------

.. literalinclude:: ../samples/os-security-groups/security-group-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/os-security-groups/security-group-update-response.json
   :language: javascript



