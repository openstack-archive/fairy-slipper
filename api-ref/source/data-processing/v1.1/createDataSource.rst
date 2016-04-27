
Create data source
==================

.. rest_method::  POST /v1.1/{tenant_id}/data-sources

Creates a data source.

Error response codes:202,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/data-sources/data-source-register-hdfs-request.json
   :language: javascript




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
   - type: type
   - id: id
   - name: name





