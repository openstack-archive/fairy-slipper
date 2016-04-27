
Create job
==========

.. rest_method::  POST /v1.1/{tenant_id}/jobs

Creates a job object.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/jobs/job-create-request.json
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





