
List projects
=============

.. rest_method::  GET /v3/projects

Lists projects.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
   - parent_id: parent_id
   - name: name
   - enabled: enabled



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - is_domain: is_domain
   - description: description
   - links: links
   - enabled: enabled
   - domain_id: domain_id
   - parent_id: parent_id
   - id: id
   - projects: projects
   - name: name




Response Example
----------------

.. literalinclude:: ../samples/admin/projects-list-response.json
   :language: javascript










