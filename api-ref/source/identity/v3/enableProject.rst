
Enable or disable project and its subtree
=========================================

.. rest_method::  PATCH /v3/projects/{project_id}/cascade

(Since v3.6) Enables or disables a project and its entire subtree.

A project subtree includes all projects beneath the parent project
in the hierarchy.

If you include attributes other than the ``enabled`` attribute,
this call fails and returns the ``Bad Request (400)`` response
code.

If you perform this action against a project that acts as a domain
(``is_domain`` is set to ``true``, this call fails and returns the
``Forbidden (403)`` response code.


Normal response codes: 200
Error response codes:413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project: project
   - enabled: enabled
   - project_id: project_id

Request Example
---------------

.. literalinclude:: ../samples/admin/project-enable-request.json
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












