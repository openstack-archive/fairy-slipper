
Password authentication with scoped authorization
=================================================

.. rest_method::  POST /v3/auth/tokens

Authenticates an identity and generates a token. Uses the password authentication method and scopes authorization to a project or domain.

The request body must include a payload that specifies the
``password`` authentication method, the credentials, and the
``project`` or ``domain`` authorization scope.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name
   - auth: auth
   - user: user
   - scope: scope
   - password: password
   - id: id
   - identity: identity
   - methods: methods
   - nocatalog: nocatalog

Request Example
---------------

.. literalinclude:: ../samples/admin/auth-password-project-scoped-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Subject-Token: X-Subject-Token
   - domain: domain
   - region_id: region_id
   - methods: methods
   - roles: roles
   - url: url
   - region: region
   - token: token
   - expires_at: expires_at
   - project: project
   - issued_at: issued_at
   - catalog: catalog
   - extras: extras
   - user: user
   - audit_ids: audit_ids
   - interface: interface
   - endpoints: endpoints
   - type: type
   - id: id
   - name: name














