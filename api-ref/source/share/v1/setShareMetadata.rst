
Set share metadata
==================

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/metadata

Sets the metadata on a share.


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

.. literalinclude:: ../samples/manila-share-set-metadata-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/manila-share-set-metadata-response.json
   :language: javascript



