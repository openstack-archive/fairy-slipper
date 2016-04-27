
Show certificate details
========================

.. rest_method::  GET /v2.1/{tenant_id}/os-certificates/{certificate_id}

Shows details for a certificate.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id
   - certificate_id: certificate_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - x-openstack-request-id: x-openstack-request-id




Response Example
----------------

.. literalinclude:: ../samples/os-certificates/certificate-show-root-response.json
   :language: javascript



