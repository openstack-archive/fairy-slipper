
Show extension details
======================

.. rest_method::  GET /v2.0/extensions/{alias}

Shows details for an extension, by alias.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - alias: alias



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

.. literalinclude:: ../samples/admin/extension-show-response.json
   :language: javascript











