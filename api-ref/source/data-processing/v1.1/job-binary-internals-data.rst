
Show job binary internal data
=============================

.. rest_method::  GET /v1.1/{tenant_id}/job-binary-internals/{job_binary_internals_id}/data

Shows data for a job binary internal.

The response body shows the job binary raw data and the response
headers show the data length.

Example response:

::

   HTTP/1.1 200 OK
   Connection: keep-alive
   Content-Length: 161
   Content-Type: text/html; charset=utf-8
   Date: Sat, 28 Mar 2016 02:21:13 GMT
   A = load '$INPUT' using PigStorage(':') as (fruit: chararray);
   B = foreach A generate com.hadoopbook.pig.Trim(fruit);
   store B into '$OUTPUT' USING PigStorage();


Normal response codes: 200
Error response codes:


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - job_binary_internals_id: job_binary_internals_id



Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - Content-Length: Content-Length




Response Example
----------------

.. literalinclude:: 
   :language: javascript



