
Create multiple servers with reservation ID
===========================================

.. rest_method::  POST /v2.1/{tenant_id}/servers

Creates one or more servers with a reservation ID.

Set ``"return_reservation_id": "True"`` in the request body to
request that a reservation ID be returned instead of the newly
created instance information. With this parameter, the response
shows only the reservation ID.

Error response codes:202,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - guest_format: guest_format
   - user_data: user_data
   - server: server
   - port: port
   - security_groups: security_groups
   - uuid: uuid
   - imageRef: imageRef
   - fixed_ip: fixed_ip
   - OS-DCF:diskConfig: OS-DCF:diskConfig
   - networks: networks
   - config_drive: config_drive
   - destination_type: destination_type
   - delete_on_termination: delete_on_termination
   - personality: personality
   - os:scheduler_hints: os:scheduler_hints
   - boot_index: boot_index
   - key_name: key_name
   - flavorRef: flavorRef
   - source_type: source_type
   - os-availability-zone:availability_zone: os-availability-zone:availability_zone
   - name: name
   - block_device_mapping_v2: block_device_mapping_v2
   - return_reservation_id: return_reservation_id
   - device_name: device_name
   - metadata: metadata
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/servers-multiple-create/multiple-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - reservation_id: reservation_id











