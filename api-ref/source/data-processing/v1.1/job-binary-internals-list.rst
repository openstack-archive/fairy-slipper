
List job binary internals
=========================

.. rest_method::  GET /v1.1/{tenant_id}/job-binary-internals

Lists the available job binary internals.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - binaries: binaries
   - name: name
   - tenant_id: tenant_id
   - created_at: created_at
   - updated_at: updated_at
   - is_protected: is_protected
   - is_public: is_public
   - datasize: datasize
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/job-binary-internals/list-response.json
   :language: javascript



