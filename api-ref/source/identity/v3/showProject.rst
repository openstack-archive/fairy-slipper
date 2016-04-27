
Show project details
====================

.. rest_method::  GET /v3/projects/{project_id}

Shows details for a project.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project_id: project_id



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

.. literalinclude:: ../samples/admin/project-show-response.json
   :language: javascript










