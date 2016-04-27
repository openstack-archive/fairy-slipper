
Generate ticket
===============

.. rest_method::  POST /v3/tickets

Generates a ticket to facilitate messaging between a source and destination.

A generate ticket request contains metadata that you specify as a
Base64-encoded JSON object and a signature.

The response shows the metadata, encrypted ticket, and signature.

Error response codes:201,413,415,405,404,403,401,400,503,409,


Request Parameters
------------------

.. rest_parameters:: parameters.yaml

   - generation: generation
   - signature: signature
   - metadata: metadata

Request Example
---------------

.. literalinclude:: ../samples/OS-KDS/ticket-generate-request.json
   :language: javascript




Response Parameters
-------------------

.. rest_parameters:: parameters.yaml

   - ticket: ticket
   - signature: signature
   - metadata: metadata














