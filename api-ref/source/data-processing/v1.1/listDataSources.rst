
List data sources
=================

.. rest_method::  GET /v1.1/{tenant_id}/data-sources

Lists all data sources.


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
   - type: type
   - id: id
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/data-sources/data-sources-list-response.json
   :language: javascript



