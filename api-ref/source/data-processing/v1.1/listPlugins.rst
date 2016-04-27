
List plugins
============

.. rest_method::  GET /v1.1/{tenant_id}/plugins

Lists all registered plugins.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - title: title
   - versions: versions
   - plugins: plugins
   - description: description
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/plugins/plugins-list-response.json
   :language: javascript



