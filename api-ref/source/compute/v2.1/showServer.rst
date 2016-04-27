
Show server details
===================

.. rest_method::  GET /v2.1/{tenant_id}/servers/{server_id}

Shows details for a server.

Includes server details including configuration drive, extended
status, and server usage information.

The extended status information appears in the ``OS-EXT-
STS:vm_state``, ``OS-EXT-STS:power_state``, and ``OS-EXT-
STS:task_state`` attributes.

The server usage information appears in the ``OS-SRV-
USG:launched_at`` and ``OS-SRV-USG:terminated_at`` attributes.

To hide ``addresses`` information for instances in a certain state,
set the ``osapi_hide_server_address_states`` configuration option.
Set this option to a valid VM state in the ``nova.conf``
configuration file.

HostId is unique **per account** and is not globally unique.

Preconditions

- The server must exist.


Normal response codes: 200
Error response codes:405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - server_id: server_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id
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

.. literalinclude:: ../samples/servers/server-show-response.json
   :language: javascript









