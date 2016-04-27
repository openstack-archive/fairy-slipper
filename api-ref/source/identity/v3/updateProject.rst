
Update project
==============

.. rest_method::  PATCH /v3/projects/{project_id}

Updates a project.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - description: description
   - enabled: enabled
   - project: project
   - parent_id: parent_id
   - domain_id: domain_id
   - name: name
   - project_id: project_id

Request Example
---------------

.. literalinclude:: ../samples/admin/project-update-request.json
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




Response Example
----------------

.. literalinclude:: ../samples/admin/project-update-response.json
   :language: javascript












