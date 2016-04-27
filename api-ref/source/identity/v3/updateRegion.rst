
Update region
=============

.. rest_method::  PATCH /v3/regions/{region_id}

Updates a region.

You can update the description or parent region ID for a region.
You cannot update the region ID.

The following error might occur:

- ``Not Found (404)``. The parent region ID does not exist.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - parent_region_id: parent_region_id
   - region: region
   - description: description
   - region_id: region_id

Request Example
---------------

.. literalinclude:: ../samples/admin/region-update-request.json
   :language: javascript




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

.. literalinclude:: ../samples/admin/region-update-response.json
   :language: javascript












