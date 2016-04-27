
Create domain
=============

.. rest_method::  POST /v3/domains

Creates a domain.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain: domain
   - enabled: enabled
   - description: description
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/admin/domain-create-request.json
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














