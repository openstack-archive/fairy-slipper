
Show job binary internal details
================================

.. rest_method::  GET /v1.1/{tenant_id}/job-binary-internals/{job_binary_internals_id}

Shows details for a job binary internal.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - job_binary_internals_id: job_binary_internals_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

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

.. literalinclude:: ../samples/job-binary-internals/show-response.json
   :language: javascript



