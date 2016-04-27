
Cancel job execution
====================

.. rest_method::  GET /v1.1/{tenant_id}/job-executions/{job_execution_id}/cancel

Cancels a job execution.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - job_execution_id: job_execution_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - info: info
   - output_id: output_id
   - start_time: start_time
   - job_id: job_id
   - updated_at: updated_at
   - tenant_id: tenant_id
   - created_at: created_at
   - args: args
   - data_source_urls: data_source_urls
   - return_code: return_code
   - oozie_job_id: oozie_job_id
   - is_protected: is_protected
   - cluster_id: cluster_id
   - end_time: end_time
   - params: params
   - is_public: is_public
   - input_id: input_id
   - configs: configs
   - job_execution: job_execution
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/job-executions/cancel-response.json
   :language: javascript



