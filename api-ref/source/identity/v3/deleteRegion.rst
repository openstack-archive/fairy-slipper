
Delete region
=============

.. rest_method::  DELETE /v3/regions/{region_id}

Deletes a region.

The following error might occur:

- ``Conflict (409)``. The region cannot be deleted because it has
  child regions.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - region_id: region_id
















