
List extensions
===============

.. rest_method::  GET /v2.0/extensions

Lists available extensions.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - alias: alias
   - updated: updated
   - description: description
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/extensions-list-response.json
   :language: javascript











