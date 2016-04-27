
Delete domain
=============

.. rest_method::  DELETE /v3/domains/{domain_id}

Deletes a domain.

To minimize the risk of accidentally deleting a domain, you must
first disable the domain by using the update domain method.

When you delete a domain, this call also deletes all entities owned
by it, such as users, groups, and projects, and any credentials and
granted roles that relate to those entities.

(Since v3.6) The deletion of a non-leaf domain in a domain
hierarchy tree is not allowed and fails with a ``Bad Request
(400)`` response code.

If you try to delete an enabled domain, this call returns the
``Forbidden (403)`` response code.

Error response codes:204,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - domain_id: domain_id
















