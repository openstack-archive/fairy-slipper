
Show resource details
=====================

.. rest_method::  GET /v2/resources/{resource_id}

Shows details for a resource, by resource ID.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - resource_id: resource_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - user_id: user_id
   - links: links
   - resource_id: resource_id
   - source: source
   - project_id: project_id
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/resource-show-response.json
   :language: javascript



