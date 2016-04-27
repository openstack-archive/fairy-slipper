
Show role details, by ID
========================

.. rest_method::  GET /v2.0/OS-KSADM/{roleId}

Shows details for a role, by ID.


Normal response codes: 200
Error response codes:203,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - roleId: roleId



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Location: Location
   - description: description
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/OS-KSADM/role-show-response.json
   :language: javascript













