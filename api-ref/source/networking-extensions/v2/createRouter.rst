
Create router
=============

.. rest_method::  POST /v2.0/routers

Creates a logical router.

This operation creates a logical router. The logical router does
not have any internal interface and it is not associated with any
subnet. You can optionally specify an external gateway for a router
at create time. The external gateway for the router must be plugged
into an external network. An external network has its
``router:external`` extended field set to ``true``. To specify an
external gateway, the UUID of the external network must be passed
in the ``external_gateway_info`` attribute in the request body, as
follows:

.. code-block:: json

   {
      "router": {
         "external_gateway_info": {
            "network_id": "8ca37218-28ff-41cb-9b10-039601ea7e6b"
         }
      }
   }

Error response codes:201,401,400,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - external_gateway_info: external_gateway_info
   - enable_snat: enable_snat
   - name: name
   - admin_state_up: admin_state_up
   - router: router
   - external_fixed_ips: external_fixed_ips

Request Example
---------------

.. literalinclude:: ../samples/routers/router-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - external_gateway_info: external_gateway_info
   - status: status
   - availability_zone_hints: availability_zone_hints
   - availability_zones: availability_zones
   - name: name
   - admin_state_up: admin_state_up
   - tenant_id: tenant_id
   - distributed: distributed
   - enable_snat: enable_snat
   - routes: routes
   - router: router
   - ha: ha
   - id: id
   - external_fixed_ips: external_fixed_ips







