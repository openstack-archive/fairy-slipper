
List share networks
===================

.. rest_method::  GET /v2/{tenant_id}/share-networks

Lists all share networks.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/manila-share-networks-list-response.json
   :language: javascript



