.. _pre_buffered_logging_pattern:

********************
Pre Buffered Logging
********************

An idiomatic pattern which buffers information which has been logged before the
actual log location and configuration is known.

:Context:
 You have an application which has to log info right from the beginning of the
 application. The location and configuration of the log shall be configurable
 application with a configuration which is read right at application startup.

:Problem:
 There may not be logged info before the location and configuration of the
 logger is known by the application.

:Solution:
 Create a logger right at the beginning of the application. Log into there until
 the logger location and configuration is known by the application. "Override"
 the pre buffer logger, log into there from now on and merge the pre buffered
 logs into the final log.
