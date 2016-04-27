
Unset share metadata
====================

.. rest_method::  DELETE /v2/{tenant_id}/shares/{share_id}/metadata/{key}

Unsets the metadata on a share.

To unset a metadata key value, specify only the key name in the
URI.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - share_id: share_id
   - tenant_id: tenant_id






Response Example
----------------

.. literalinclude:: 
   :language: javascript



