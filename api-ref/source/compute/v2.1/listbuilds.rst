
List agent builds
=================

.. rest_method::  GET /v2.1/{tenant_id}/os-agents

Lists agent builds.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-agents/agents-list-response.json
   :language: javascript



