
Create group
============

.. rest_method::  POST /v3/groups/{name}

Creates a group in the KDS.

Membership in groups is based on the party name. For example, a
``scheduler`` group implicitly includes any party name that starts
with ``scheduler``. For example, a member named
``scheduler.host.example.com``.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - name: name



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - name: name














