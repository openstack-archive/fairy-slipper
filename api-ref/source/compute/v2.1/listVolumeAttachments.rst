
List volume attachments
=======================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-volume_attachments

Lists the volume attachments for a server.


Normal response codes: 200
Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id






Response Example
----------------

.. literalinclude:: ../samples/os-volumes/list-volume-attachments-resp.json
   :language: javascript











