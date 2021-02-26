# timework

[![pypi](https://img.shields.io/pypi/v/timework)](https://pypi.org/project/timework/)
[![codefactor](https://www.codefactor.io/repository/github/bugstop/python-timework/badge)](https://www.codefactor.io/repository/github/bugstop/python-timework)
[![coverage](https://coveralls.io/repos/github/bugstop/python-timework/badge.svg?branch=master)](https://coveralls.io/github/bugstop/python-timework?branch=master)
[![platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-red)](https://github.com/bugstop/python-timework)

measure / limit execution time using with-statements or decorators, cross-platform

## Install

```bash
pip install timework
```

## Usage

```python
import timework as tw
```

### Statement `with`

#### timework.Stopwatch

> measure execution time

##### Example

```python
with tw.Stopwatch() as s:
    s.split()
    s.stop()
    s.restart()
    s.pause()
    s.resume()
    s.get_sec()
    s.get_hms()
```

##### Functions

```
get_sec()  get_hms()  restart()  pause()
resume()   split()    stop()
```

### Decorator `@`

#### timework.timer

> measure execution time

##### Example

```python
@tw.timer(logging.warning)
def your_function():
    ...
```

##### Arguments

```
output: A function object that specifies where to log messages.
        For example: print. timework.nil does not log messages.
detail: A boolean value, whether to print start and end time.
        This argument must be passed using keywords.
```

#### timework.limit

> limit execution time

##### Example

```python
@tw.limit(3)
def your_function():
    ...
```

##### Arguments

```
timeout: This argument sets the timeout limit of the decorated
         function. Once the run time of the process reaches
         [timeout] seconds but not yet finishes, then raise
         TimeoutException and stop the inner function.
```

## License

MIT License &copy; <a href="https://github.com/bugstop" style="color: black !important; text-decoration: none !important;">bugstop</a>
