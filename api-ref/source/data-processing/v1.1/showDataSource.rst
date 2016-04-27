
Show data source details
========================

.. rest_method::  GET /v1.1/{tenant_id}/data-sources/{data_source_id}

Shows details for a data source.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - data_source_id: data_source_id



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




Response Example
----------------

.. literalinclude:: ../samples/data-sources/data-source-show-response.json
   :language: javascript



