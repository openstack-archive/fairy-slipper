
List access rules
=================

.. rest_method::  POST /v2/{tenant_id}/shares/{share_id}/action

Lists access rules for a share.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - access_list: access_list
   - share_id: share_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-actions-list-access-rules-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - access_type: access_type
   - access_to: access_to
   - access_level: access_level
   - state: state
   - access_list: access_list
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/manila-share-actions-list-access-rules-response.json
   :language: javascript



