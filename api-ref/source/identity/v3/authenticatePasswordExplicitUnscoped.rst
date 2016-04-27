
Password authentication with explicit unscoped authorization
============================================================

.. rest_method::  POST /v3/auth/tokens

Authenticates an identity and generates a token. Uses the password authentication method with explicit unscoped authorization.

The request body must include a payload that specifies the
``password`` authentication method, the credentials, and the
``unscoped`` authorization scope.

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

.. literalinclude:: ../samples/admin/auth-password-explicit-unscoped-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Subject-Token: X-Subject-Token
   - domain: domain
   - methods: methods
   - roles: roles
   - expires_at: expires_at
   - token: token
   - extras: extras
   - user: user
   - audit_ids: audit_ids
   - issued_at: issued_at
   - id: id
   - name: name














