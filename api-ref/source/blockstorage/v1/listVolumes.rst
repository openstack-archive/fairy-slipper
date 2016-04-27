
List volumes
============

.. rest_method::  GET /v1/{tenant_id}/volumes

Lists all volumes.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - volumes: volumes
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/volumes/volumes-list-response.json
   :language: javascript



