
Show meter statistics
=====================

.. rest_method::  GET /v2/meters/{meter_name}/statistics

Computes and lists statistics for samples in a time range.


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - meter_name: meter_name
   - q: q
   - groupby: groupby
   - period: period
   - aggregate: aggregate
   - limit: limit



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - count: count
   - duration_start: duration_start
   - min: min
   - max: max
   - duration_end: duration_end
   - period: period
   - sum: sum
   - duration: duration
   - period_end: period_end
   - aggregate: aggregate
   - period_start: period_start
   - avg: avg
   - groupby: groupby
   - unit: unit




Response Example
----------------

.. literalinclude:: ../samples/statistics-list-response.json
   :language: javascript



