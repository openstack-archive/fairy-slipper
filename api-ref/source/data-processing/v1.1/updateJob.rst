
Update job object
=================

.. rest_method::  PATCH /v1.1/{tenant_id}/jobs/{job_id}

Updates a job object.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - job_id: job_id

Request Example
---------------

.. literalinclude:: ../samples/jobs/job-update-request.json
   :language: javascript




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





