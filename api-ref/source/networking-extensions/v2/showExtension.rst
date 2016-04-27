
Show extension details
======================

.. rest_method::  GET /v2.0/extensions/{alias}

Shows details for an extension, by alias.


Normal response codes: 200
Error response codes:203,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - alias: alias



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

.. literalinclude:: ../samples/extensions/extension-show-response.json
   :language: javascript




