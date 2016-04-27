
Create region
=============

.. rest_method::  POST /v3/regions

Creates a region.

When you create the region, you can optionally specify a region ID.
If you include characters in the region ID that are not allowed in
a URI, you must URL-encode the ID. If you omit an ID, the API
assigns an ID to the region.

The following errors might occur:

- ``Not Found (404)``. The parent region ID does not exist.

- ``Conflict (409)``. The parent region ID would form a circular
  relationship.

- ``Conflict (409)``. The user-defined region ID is not unique to
  the OpenStack deployment.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - parent_region_id: parent_region_id
   - region: region
   - description: description
   - id: id

Request Example
---------------

.. literalinclude:: ../samples/admin/region-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - parent_region_id: parent_region_id
   - region: region
   - description: description
   - links: links
   - id: id














