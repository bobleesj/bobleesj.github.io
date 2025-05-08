---
layout: post
title: Intro to Python logging for beginners (Ft. logging)
categories: tutorial
---

## Motivation

Logs record activities. They are used for debugging and analyzing user behavior.
While `print()` serves as a perfectly good solution for simple programs, there
are specific needs that it cannot fulfill:

- Saving logs in a separate folder or periodically
- Turning on/off certain types of logs globally
- Providing information on line numbers, file names, etc.
- Categorizing logs into `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`

For these requirements, we may want to use Python's built-in logging tool.

## Initial Setup

First, copy the following code to a Python file:

```python
import logging

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

if __name__ == "__main__":
    main()
```

Add log messages by modifying the file like this:

```python
import logging

def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    logging.debug("This is a debug log.")
    logging.info("This is an info log.")
    logging.warning("This is a warning log.")
    logging.error("This is an error log.")
    logging.critical("This is a critical log.")

if __name__ == "__main__":
    main()
```

## Understand log levels

The log level `DEBUG` is the lowest, meaning all messages from all severity
levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`) will be logged. Refer
to the table below:

| Log Level Set | Messages Printed                      |
| ------------- | ------------------------------------- |
| DEBUG         | DEBUG, INFO, WARNING, ERROR, CRITICAL |
| INFO          | INFO, WARNING, ERROR, CRITICAL        |
| WARNING       | WARNING, ERROR, CRITICAL              |
| ERROR         | ERROR, CRITICAL                       |
| CRITICAL      | CRITICAL                              |

For example, if you modify from `logging.DEBUG` to `logging.ERROR`

```text
python main.py (logging.DEBUG)
2024-05-23 16:28:07 INFO This is an info log.
2024-05-23 16:28:07 WARNING This is a warning log.
2024-05-23 16:28:07 ERROR This is an error log.
2024-05-23 16:28:07 CRITICAL This is a critical log.

python main.py (logging.ERROR)
2024-05-23 16:28:14 ERROR This is an error log.
2024-05-23 16:28:14 CRITICAL This is a critical log.
```

## Save logs

Modify the `basicConfig` by adding `filename` and `filemode`.

```python
logging.basicConfig(
    level=logging.DEBUG,
    filename='app.log',
    filemode='w',  # 'w' to write, 'a' to append
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

```

As of this writing, I currently have no further solutions needed beyond the
above at the current level. I may add more details if more advanced
functionalities from the `logging` library are needed for my projects.
