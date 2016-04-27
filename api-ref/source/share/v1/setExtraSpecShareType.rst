
Set extra spec for share type
=============================

.. rest_method::  POST /v2/{tenant_id}/types/{share_type_id}/extra_specs

Sets an extra specification for the share type.

Each driver implementation determines which extra specification
keys it uses. For details, see `Capabilities and Extra-Specs <http:
//docs.openstack.org/developer/manila/devref/capabilities_and_extra
_specs.html>`_ and documentation for your driver.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - extra_specs: extra_specs
   - share_type_id: share_type_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/manila-share-type-set-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - extra_specs: extra_specs




Response Example
----------------

.. literalinclude:: ../samples/manila-share-type-set-response.json
   :language: javascript



