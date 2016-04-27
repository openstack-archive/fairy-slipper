
Update share metadata
=====================

.. rest_method::  PUT /v2/{tenant_id}/shares/{share_id}/metadata

Updates the metadata for a share.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata
   - share_id: share_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-update-metadata-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/manila-share-update-metadata-response.json
   :language: javascript



