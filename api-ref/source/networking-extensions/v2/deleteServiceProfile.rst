
Delete service profile
======================

.. rest_method::  DELETE /v2.0/service_profiles/{profile_id}

Deletes a service profile.

Attempting to delete a service profile that is currently associated
with a flavor will return a ``Conflict 409`` with a response body
containing an in use message.

Error response codes:409,404,403,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - profile_id: profile_id











