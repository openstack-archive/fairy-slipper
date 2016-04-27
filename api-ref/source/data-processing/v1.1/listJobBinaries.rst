
List job binaries
=================

.. rest_method::  GET /v1.1/{tenant_id}/job-binaries

Lists the available job binaries.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - url: url
   - tenant_id: tenant_id
   - created_at: created_at
   - updated_at: updated_at
   - is_protected: is_protected
   - is_public: is_public
   - binaries: binaries
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/job-binaries/list-response.json
   :language: javascript



