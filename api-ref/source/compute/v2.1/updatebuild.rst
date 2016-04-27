
Update agent build
==================

.. rest_method::  PUT /v2.1/{tenant_id}/os-agents/{agent_build_id}

Updates an agent build.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - url: url
   - md5hash: md5hash
   - version: version
   - agent_build_id: agent_build_id
   - tenant_id: tenant_id

Request Example
---------------

.. literalinclude:: ../samples/os-agents/agent-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - url: url
   - md5hash: md5hash
   - agent_id: agent_id
   - version: version




Response Example
----------------

.. literalinclude:: ../samples/os-agents/agent-update-response.json
   :language: javascript



