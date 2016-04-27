
Delete project subtree
======================

.. rest_method::  DELETE /v3/projects/{project_id}/cascade

(Since v3.6) Deletes a project and its entire subtree.

A project subtree includes all projects beneath the parent project
in the hierarchy. You must disable the projects in the subtree
before you perform this operation.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - project_id: project_id
















