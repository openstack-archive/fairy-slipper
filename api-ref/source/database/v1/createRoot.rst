
Enable root user
================

.. rest_method::  POST /v1.0/{accountId}/instances/{instanceId}/root

Enables the root user for a database instance and returns the root password.

This operation generates a root password for the root user and
enables the root user to log in from any host.

Changes that you make as a root user can impact the database
instance and API operations in unpredictable and detrimental ways.
When you enable the root user, you accept the possibility that we
cannot support your database instance. We might not be able to
assist you if you change core MySQL settings. These changes can be,
but are not limited to, turning off bin logs, removing users that
we use to access your instance, and so on.


Normal response codes: 200
Error response codes:413,405,404,403,401,400,422,503,500,501,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - instanceId: instanceId
   - accountId: accountId






Response Example
----------------

.. literalinclude:: samples/db-enable-root-user-response.json
   :language: javascript













