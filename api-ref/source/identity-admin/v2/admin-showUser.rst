
Show user details
=================

.. rest_method::  GET /v2.0/users/{userId}

Shows details for a user, by ID.

The `openstack user show <http://docs.openstack.org/cli-
reference/openstack.html#openstack-user-show>`_ command supports
showing user details by name or ID. However, the command actually
looks up the user ID for a user name and queries the user by ID.

As a workaround, complete these steps to show details for a user by
name:

- `List all users <http://developer.openstack.org/api-ref-identity-
  admin-v2.html#admin-listUsers>`_.

- In the response, find the user name for which you want to show
  details and note its corresponding user ID.

- `Show details for user <http://developer.openstack.org/api-ref-
  identity-admin-v2.html#admin-showUser>`_.


Normal response codes: 200
Error response codes:203,413,405,404,403,401,400,503,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - userId: userId



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - username: username
   - enabled: enabled
   - email: email
   - name: name
   - id: id




Response Example
----------------

.. literalinclude:: ../samples/admin/user-show-response.json
   :language: javascript











