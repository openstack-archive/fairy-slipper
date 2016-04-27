
Create job binary internal
==========================

.. rest_method::  PUT /v1.1/{tenant_id}/job-binary-internals/{name}

Creates a job binary internal.

Job binary internals are objects that represent data processing
applications and libraries that are stored in the internal
database.

Specify the file contents (raw data or script text) in the request
body. Specify the file name in the URI.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name



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





