
List volumes
============

.. rest_method::  GET /v2/{tenant_id}/volumes

Lists summary information for all Block Storage volumes that the tenant can access.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - sort: sort
   - limit: limit
   - marker: marker



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



