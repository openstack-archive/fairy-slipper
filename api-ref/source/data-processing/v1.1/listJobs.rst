
List jobs
=========

.. rest_method::  GET /v1.1/{tenant_id}/jobs

Lists all jobs.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - jobs: jobs
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

.. literalinclude:: ../samples/jobs/jobs-list-response.json
   :language: javascript



