
Show extension details
======================

.. rest_method::  GET /v2.1/{tenant_id}/extensions/{alias}

Shows details for an extension, by alias.


Normal response codes: 200
Error response codes:203,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - alias: alias



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - updated: updated
   - description: description
   - links: links
   - namespace: namespace
   - alias: alias
   - extension: extension
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/extensions/extension-show-response.json
   :language: javascript




