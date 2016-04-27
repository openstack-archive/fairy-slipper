
List extensions
===============

.. rest_method::  GET /v2.0/extensions

Lists available extensions.

Extensions introduce features and vendor-specific functionality to
the API.

The response shows the extension name and its alias. To show
details for an extension, you specify the alias.


Normal response codes: 200
Error response codes:203,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - updated: updated
   - description: description
   - links: links
   - alias: alias
   - extension: extension
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/extensions/extensions-list-response.json
   :language: javascript




