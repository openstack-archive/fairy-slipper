
Extend share
============

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Increases the size of a share.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - new_size: new_size
   - share_id: share_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-actions-extend-request.json
   :language: javascript








