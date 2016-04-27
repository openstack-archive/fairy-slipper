
Show job details
================

.. rest_method::  GET /v1.1/{tenant_id}/jobs/{job_id}

Shows details for a job.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - job_id: job_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - tenant_id: tenant_id
   - created_at: created_at
   - mains: mains
   - updated_at: updated_at
   - libs: libs
   - is_protected: is_protected
   - interface: interface
   - is_public: is_public
   - type: type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/jobs/job-show-response.json
   :language: javascript



