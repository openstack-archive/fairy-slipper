Tempest Examples
================

To back fill the missing examples from the WADL, tempest result logs
can be used.

If you run tempest with a `logging.conf` like.  The one below then the
resulting log `requests.log` will be suitable for processing.

::

   [loggers]
   keys=root,tempest_http

   [handlers]
   keys=file,devel

   [formatters]
   keys=simple,dumb

   [logger_root]
   level=DEBUG
   handlers=devel

   [logger_tempest_http]
   level=DEBUG
   handlers=file
   qualname=tempest_lib.common.rest_client

   [handler_file]
   class=FileHandler
   level=DEBUG
   args=('requests.log', 'w+')
   formatter=dumb

   [handler_devel]
   class=StreamHandler
   level=INFO
   args=(sys.stdout,)
   formatter=simple

   [formatter_simple]
   format=%(asctime)s.%(msecs)03d %(process)d %(levelname)s: %(message)s

   [formatter_dumb]
   format=%(message)s


Once the tempest run has completed, you can then process the log into
a format for the WADL conversion process.  This is done using the `fairy-slipper-tempest-log` tool::

  fairy-slipper-tempest-log -o conversion_files/ requests.log

Where `conversion_files/` is the directory you are using to store the
intermediate files during the migration from docbook.
