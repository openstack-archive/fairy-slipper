
List regions
============

.. rest_method::  GET /v3/regions

Lists regions.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - parent_region_id: parent_region_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - regions: regions
   - parent_region_id: parent_region_id
   - description: description
   - links: links
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/regions-list-response.json
   :language: javascript










