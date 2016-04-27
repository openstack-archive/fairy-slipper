
Show region details
===================

.. rest_method::  GET /v3/regions/{region_id}

Shows details for a region, by ID.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - region_id: region_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - parent_region_id: parent_region_id
   - region: region
   - description: description
   - links: links
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/region-show-response.json
   :language: javascript










