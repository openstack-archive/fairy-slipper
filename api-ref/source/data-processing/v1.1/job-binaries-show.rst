
Show job binary details
=======================

.. rest_method::  GET /v1.1/{tenant_id}/job-binaries

Shows details for a job binary.


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
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/job-binaries/show-response.json
   :language: javascript



