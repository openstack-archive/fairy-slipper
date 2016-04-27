
List backups
============

.. rest_method::  GET /v2/{tenant_id}/backups

Lists Block Storage backups to which the tenant has access.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - sort_key: sort_key
   - sort_dir: sort_dir
   - limit: limit
   - marker: marker



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - backups: backups
   - id: id
   - links: links
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/backups/backups-list-response.json
   :language: javascript



