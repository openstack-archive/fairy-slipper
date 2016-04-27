
Create security group
=====================

.. rest_method::  POST /v2.1/{tenant_id}/os-security-groups

Creates a security group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - security_group: security_group
   - description: description
   - name: name
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-security-groups/security-group-create-request.json
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

.. literalinclude:: ../samples/os-security-groups/security-group-create-response.json
   :language: javascript



