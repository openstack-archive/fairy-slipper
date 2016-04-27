
Update security group
=====================

.. rest_method::  PUT /v2.0/security-groups/{security_group_id}

Updates a security group.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - name: name
   - security_group_id: security_group_id

Request Example
---------------

.. literalinclude:: ../samples/security-groups/security-group-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - security_group: security_group
   - tenant_id: tenant_id
   - description: description
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/security-groups/security-group-update-response.json
   :language: javascript










