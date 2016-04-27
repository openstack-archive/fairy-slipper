
Show volume attachment details
==============================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}/os-volume_attachments/{attachment_id}

Shows details for a volume attachment.

Preconditions

- The volume must be attached to the server.


Normal response codes: 200
Error response codes:415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id
   - attachment_id: attachment_id






Response Example
----------------

.. literalinclude:: ../samples/os-volumes/volume-attachment-detail-response.json
   :language: javascript











