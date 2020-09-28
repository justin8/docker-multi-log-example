# Multi-log Example

The point of this example is to show a way to export multiple log files from a container workload. Typically you would want to use STDOUT/STDERR for this, but some workloads require third party applications where you do not have control over how the log, or they emit more than one or two distinct streams. In this scenario publishing via the standardized Docker log output methods is not feasible. This is one solution to that problem.

## Solution

In this solution we are logging to multiple files, we have a python script in a docker container pumping out 2 streams of rotating log files to emulate a more realistic workload. From here we start a dummy container for each log file/stream which we can then log from whatever container orchestration framework you are using. e.g. with AWS ECS you can enable cloudwatch logs on the individual containers as a part of the task definition. Similar methods can be used for other loggers.

Another alternative is to run your logging agent in a sidecar container that pushes the log streams itself, this solution relies on the built-in methods to allow better integration with native tooling instead.

## Usage

This example can be spun up using `docker-compose up -d`. You can then view the different streams with `docker-compose logs -f`. You can use a similar method with any container orchestration platform to co-ordinate the logging output containers.

### Caveats

- Each logging process will consume roughly 1-2MB of extra ram, however this is typically negligible to most workloads
- GNU tail will print informational messages about the log file status to the stream that cannot be turned off, e.g:
  - `tail: cannot open '/logs/first_logfile.log' for reading: No such file or directory`
  - `tail: '/logs/first_logfile.log' has been replaced; following new file`
