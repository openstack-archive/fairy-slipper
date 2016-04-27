
List extensions
===============

.. rest_method::  GET /v2.1/{tenant_id}/extensions

Lists available extensions.

Extensions introduce features and vendor-specific functionality to
the API without requiring a version change.

The response shows the extension name and its alias. To show
details for an extension, you specify the alias.


Normal response codes: 200
Error response codes:203,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
   - updated: updated
   - description: description
   - links: links
   - namespace: namespace
   - alias: alias
   - extensions: extensions
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/extensions/extensions-list-response.json
   :language: javascript




