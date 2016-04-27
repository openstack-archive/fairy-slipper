
Password authentication with unscoped authorization
===================================================

.. rest_method::  POST /v3/auth/tokens

Authenticates an identity and generates a token. Uses the password authentication method. Authorization is unscoped.

The request body must include a payload that specifies the
authentication method, which is ``password``, and the user, by ID
or name, and password credentials.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain: domain
   - name: name
   - auth: auth
   - user: user
   - password: password
   - id: id
   - identity: identity
   - methods: methods
   - nocatalog: nocatalog

Request Example
---------------

.. literalinclude:: ../samples/admin/auth-password-unscoped-request-with-domain.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - X-Subject-Token: X-Subject-Token
   - domain: domain
   - methods: methods
   - expires_at: expires_at
   - token: token
   - extras: extras
   - user: user
   - audit_ids: audit_ids
   - issued_at: issued_at
   - id: id
   - name: name














