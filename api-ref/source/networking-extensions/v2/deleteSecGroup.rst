
Delete security group
=====================

.. rest_method::  DELETE /v2.0/security-groups/{security_group_id}

Deletes an OpenStack Networking security group.

This operation deletes an OpenStack Networking security group and
its associated security group rules, provided that a port is not
associated with the security group.

This operation does not require a request body. This operation does
not return a response body.

Error response codes:409,404,204,401,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - security_group_id: security_group_id










