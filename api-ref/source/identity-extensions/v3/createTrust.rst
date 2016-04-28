
Create trust
============

.. rest_method::  POST /v3/OS-TRUST/trusts

Creates a trust.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - impersonation: impersonation
   - trust: trust
   - trustor_user_id: trustor_user_id
   - name: name
   - roles: roles
   - oauth_expires_at: oauth_expires_at
   - remaining_uses: remaining_uses
   - trustee_user_id: trustee_user_id
   - project_id: project_id

Request Example
---------------

.. literalinclude:: ../samples/OS-TRUST/trust-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - impersonation: impersonation
   - roles_links: roles_links
   - trust: trust
   - trustor_user_id: trustor_user_id
   - name: name
   - links: links
   - oauth_expires_at: oauth_expires_at
   - remaining_uses: remaining_uses
   - trustee_user_id: trustee_user_id
   - roles: roles
   - project_id: project_id
   - id: id














