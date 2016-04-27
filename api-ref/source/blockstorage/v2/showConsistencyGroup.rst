
Show consistency group details
==============================

.. rest_method::  GET /v2/{tenant_id}/consistencygroups/{consistencygroup_id}

Shows details for a consistency group.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - consistencygroup_id: consistencygroup_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - status: status
   - description: description
   - availability_zone: availability_zone
   - created_at: created_at
   - volume_types: volume_types
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/consistencygroups/consistency-group-show-response.json
   :language: javascript



