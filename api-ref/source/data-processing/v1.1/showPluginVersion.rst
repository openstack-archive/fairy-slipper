
Show plugin version details
===========================

.. rest_method::  GET /v1.1/{tenant_id}/plugins/{plugin_name}/{version}

Shows details for a plugin version.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - version: version
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

.. literalinclude:: ../samples/plugins/plugin-version-show-response.json
   :language: javascript



