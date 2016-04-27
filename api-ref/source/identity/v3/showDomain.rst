
Show domain details
===================

.. rest_method::  GET /v3/domains/{domain_id}

Shows details for a domain.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id



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

.. literalinclude:: ../samples/admin/domain-show-response.json
   :language: javascript










