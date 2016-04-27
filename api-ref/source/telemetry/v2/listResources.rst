
List resources
==============

.. rest_method::  GET /v2/resources

Lists definitions for all resources.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - q: q
   - meter_links: meter_links



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

.. literalinclude:: ../samples/resources-list-response.json
   :language: javascript



