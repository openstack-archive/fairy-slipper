
Create server
=============

.. rest_method::  POST /v2.1/{tenant_id}/servers

Creates a server.

The progress of this operation depends on the location of the
requested image, network I/O, host load, selected flavor, and other
factors.

To check the progress of the request, make a ``GET /servers/{id}``
request. This call returns a progress attribute, which is a
percentage value from 0 to 100.

The ``Location`` header returns the full URL to the newly created
server and is available as a ``self`` and ``bookmark`` link in the
server representation.

When you create a server, the response shows only the server ID,
its links, and the admin password. You can get additional
attributes through subsequent GET requests on the server.

Include the ``block-device-mapping-v2`` parameter in the create
request body to boot a server from a volume.

Include the ``key_name`` parameter in the create request body to
add a keypair to the server when you create it. To create a
keypair, make a `create keypair <http://developer.openstack.org
/api-ref-compute-v2.1.html#createKeypair>`_ request.

Preconditions

- The user must have sufficient server quota to create the number of
  servers requested.

- The connection to the Image service is valid.

Asynchronous postconditions

- With correct permissions, you can see the server status as
  ``ACTIVE`` through API calls.

- With correct access, you can see the created server in the compute
  node that OpenStack Compute manages.

Troubleshooting

- If the server status remains ``BUILDING`` or shows another error
  status, the request failed. Ensure you meet the preconditions
  then investigate the compute node.

- The server is not created in the compute node that OpenStack
  Compute manages.

- The compute node needs enough free resource to match the resource
  of the server creation request.

- Ensure that the scheduler selection filter can fulfill the request
  with the available compute nodes that match the selection
  criteria of the filter.

Error response codes:202,405,404,403,401,400,503,


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

Request Example
---------------

.. literalinclude:: ../samples/servers/server-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - links: links
   - adminPass: adminPass
   - OS-DCF:diskConfig: OS-DCF:diskConfig
   - server: server
   - id: id
   - security_groups: security_groups











