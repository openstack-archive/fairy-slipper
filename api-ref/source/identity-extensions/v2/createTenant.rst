
Create tenant
=============

.. rest_method::  POST /v2.0/tenants

Creates a tenant.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml


Request Example
---------------

.. literalinclude:: ../samples/OS-KSADM/tenantwithoutid-create-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - tenant: tenant
   - enabled: enabled
   - description: description
   - name: name
   - id: id














