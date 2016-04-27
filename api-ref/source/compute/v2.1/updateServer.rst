
Update server
=============

.. rest_method::  PUT /v2.1/{tenant_id}/servers/{server_id}

Updates the editable attributes of a server.

Preconditions

- The server must exist.

- You can edit the ``accessIPv4``, ``accessIPv6``, ``diskConfig``
  and ``name`` attributes.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - guest_format: guest_format
   - user_data: user_data
   - device_name: device_name
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
   - server: server
   - metadata: metadata
   - tenant_id: tenant_id
   - server_id: server_id

Request Example
---------------

.. literalinclude:: ../samples/servers/server-update-diskconfig-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - OS-EXT-STS:task_state: OS-EXT-STS:task_state
   - addresses: addresses
   - links: links
   - image: image
   - OS-EXT-STS:vm_state: OS-EXT-STS:vm_state
   - OS-EXT-SRV-ATTR:instance_name: OS-EXT-SRV-ATTR:instance_name
   - OS-SRV-USG:launched_at: OS-SRV-USG:launched_at
   - flavor: flavor
   - id: id
   - security_groups: security_groups
   - description: description
   - os-extended-volumes:volumes_attached: os-extended-volumes:volumes_attached
   - user_id: user_id
   - OS-DCF:diskConfig: OS-DCF:diskConfig
   - progress: progress
   - OS-EXT-STS:power_state: OS-EXT-STS:power_state
   - OS-EXT-AZ:availability_zone: OS-EXT-AZ:availability_zone
   - metadata: metadata
   - status: status
   - updated: updated
   - hostId: hostId
   - OS-EXT-SRV-ATTR:host: OS-EXT-SRV-ATTR:host
   - OS-SRV-USG:terminated_at: OS-SRV-USG:terminated_at
   - rules: rules
   - key_name: key_name
   - OS-EXT-SRV-ATTR:hypervisor_hostname: OS-EXT-SRV-ATTR:hypervisor_hostname
   - name: name
   - created: created
   - tenant_id: tenant_id
   - server: server
   - host_status: host_status




Response Example
----------------

.. literalinclude:: ../samples/servers/server-update-response.json
   :language: javascript










