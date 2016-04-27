
Create project
==============

.. rest_method::  POST /v3/projects

Creates a project.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - is_domain: is_domain
   - description: description
   - enabled: enabled
   - project: project
   - parent_id: parent_id
   - domain_id: domain_id
   - name: name

Request Example
---------------

.. literalinclude:: ../samples/admin/project-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - is_domain: is_domain
   - description: description
   - links: links
   - enabled: enabled
   - domain_id: domain_id
   - project: project
   - parent_id: parent_id
   - id: id
   - name: name














