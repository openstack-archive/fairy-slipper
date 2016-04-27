
Authenticate for admin API
==========================

.. rest_method::  POST /v2.0/tokens

Authenticates and generates a token.

A REST interface provides client authentication by using the POST
method with ``v2.0/tokens`` as the path. Include a payload of
credentials in the body.

The Identity API is a RESTful web service. It is the entry point to
all service APIs. To access the Identity API, you must know its
URL.

Each REST request against the Identity Service requires the ``X
-Auth-Token`` header. Clients obtain this token and the URL
endpoints for other service APIs by supplying their valid
credentials to the authentication service.

If the authentication token has expired, this call returns the HTTP
``unauthorized (401)`` response code.

If the token has expired, this call returns the ``itemNotFound
(404)`` response code.

The Identity API treats expired tokens as no longer valid tokens.

The deployment determines how long expired tokens are stored.

To view the ``trust`` object, you need to set ``trust`` enable on
the keystone configuration.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/admin/authenticate-token-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - impersonation: impersonation
   - endpoints_links: endpoints_links
   - serviceCatalog: serviceCatalog
   - description: description
   - type: type
   - expires: expires
   - enabled: enabled
   - name: name
   - access: access
   - trustee_user_id: trustee_user_id
   - token: token
   - user: user
   - issued_at: issued_at
   - trustor_user_id: trustor_user_id
   - endpoints: endpoints
   - trust: trust
   - id: id
   - tenant: tenant
   - metadata: metadata




Response Example
----------------

.. literalinclude:: ../samples/admin/authenticate-response.json
   :language: javascript











