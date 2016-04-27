
List share limits
=================

.. rest_method::  GET /v2/{tenant_id}/limits

Lists share limits.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - tenant_id: tenant_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - regex: regex
   - verb: verb
   - totalShareNetworksUsed: totalShareNetworksUsed
   - maxTotalShareGigabytes: maxTotalShareGigabytes
   - maxTotalShareNetworks: maxTotalShareNetworks
   - totalSharesUsed: totalSharesUsed
   - uri: uri
   - value: value
   - totalShareGigabytesUsed: totalShareGigabytesUsed
   - totalShareSnapshotsUsed: totalShareSnapshotsUsed
   - next-available: next-available
   - unit: unit
   - maxTotalShares: maxTotalShares
   - totalSnapshotGigabytesUsed: totalSnapshotGigabytesUsed
   - maxTotalSnapshotGigabytes: maxTotalSnapshotGigabytes
   - remaining: remaining
   - maxTotalShareSnapshots: maxTotalShareSnapshots




Response Example
----------------

.. literalinclude:: ../samples/manila-limits-response.json
   :language: javascript



