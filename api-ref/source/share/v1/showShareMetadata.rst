
Show share metadata
===================

.. rest_method::  GET /v2/{tenant_id}/shares/{share_id}/metadata

Shows the metadata for a share.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - share_id: share_id
   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/manila-share-show-metadata-response.json
   :language: javascript



