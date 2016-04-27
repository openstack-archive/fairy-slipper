
List job types
==============

.. rest_method::  GET /v1.1/{tenant_id}/job-types

Lists all job types.

You can use query parameters to filter the response.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - plugin: plugin
   - version: version
   - type: type
   - hints: hints



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - versions: versions
   - title: title
   - description: description
   - job_types: job_types
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/job-types/job-types-list-response.json
   :language: javascript



