
Update domain
=============

.. rest_method::  PATCH /v3/domains/{domain_id}

Updates a domain.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain: domain
   - enabled: enabled
   - description: description
   - name: name
   - domain_id: domain_id

Request Example
---------------

.. literalinclude:: ../samples/admin/domain-update-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - domain: domain
   - name: name
   - links: links
   - enabled: enabled
   - id: id
   - description: description




Response Example
----------------

.. literalinclude:: ../samples/admin/domain-update-response.json
   :language: javascript












