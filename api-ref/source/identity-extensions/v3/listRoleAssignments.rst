
List role assignments
=====================

.. rest_method::  GET /v3/role_assignments

Lists role assignments.

The scope section in the list response is extended to allow the
representation of role assignments that are inherited to projects.

The list of all role assignments can be long. To filter the list,
use the query parameters.

Some typical examples are:

``GET /role_assignments?user.id={user_id}`` lists all role
assignments for a user.

``GET /role_assignments?scope.project.id={project_id}`` lists all
role assignments for a project.

Each role assignment entity in the collection contains a link to
the assignment that created this entity.

Use the ``effective`` query parameter to list effective assignments
at the user, project, and domain level. This parameter allows for
the effects of group membership as well as inheritance from the
parent domain or project, for role assignments that were made using
OS-INHERIT assignment APIs.

The group role assignment entities themselves are not returned in
the collection. Because, like group membership, the effects of
inheritance have already been allowed for, the role assignment
entities themselves that specify the inheritance are not returned
in the collection. This represents the effective role assignments
that would be included in a scoped token. You can use the other
query parameters with the ``effective`` parameter.

For example, to determine what a user can actually do, issue this
request: ``GET /role_assignments?user.id={user_id} & effective``

To get the equivalent set of role assignments that would be
included in the token response of a project-scoped token, issue
``GET /role_assignments?user.id={user_id} &
scope.project.id={project_id} & effective``

In the response, the entity ``links`` section for entities that are
included by virtue of group members also contains a url that you
can use to access the membership of the group.

Use the ``scope.OS-INHERIT:inherited_to`` query parameter to filter
the response by inherited role assignments. The ``scope.OS-
INHERIT:inherited_to`` value of ``projects`` is currently
supported. This value indicates that this role is inherited to all
projects of the owning domain or parent project.

An example response for an API call with the ``effective`` query
string:


Normal response codes: 200
Error response codes:413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml







Response Example
----------------

.. literalinclude:: ../samples/OS-INHERIT/role-assignments-effective-list-response.json
   :language: javascript










