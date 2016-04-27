
Show plugin details
===================

.. rest_method::  GET /v1.1/{tenant_id}/plugins/{plugin_name}

Shows details for a plugin.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - plugin_name: plugin_name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - versions: versions
   - title: title
   - description: description
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/plugins/plugin-show-response.json
   :language: javascript



