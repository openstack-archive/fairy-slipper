
List security groups
====================

.. rest_method::  GET /v2.1/{tenant_id}/os-security-groups

Lists security groups.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - rules: rules
   - tenant_id: tenant_id
   - id: id
   - security_groups: security_groups
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/os-security-groups/security-groups-list-response.json
   :language: javascript



