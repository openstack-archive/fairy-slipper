
List flavors with details
=========================

.. rest_method::  GET /v2.1/{tenant_id}/flavors/detail

Lists flavors with details.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - minDisk: minDisk
   - minRam: minRam
   - sort_key: sort_key
   - sort_dir: sort_dir
   - limit: limit
   - marker: marker



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/flavors/flavors-list-detail-response.json
   :language: javascript



