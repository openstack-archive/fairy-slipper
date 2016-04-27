
Show role information by name
=============================

.. rest_method::  GET /v2.0/OS-KSADM/roles/{role_name}

Shows information for a role, by name.


Normal response codes: 200
Error response codes:203,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




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













