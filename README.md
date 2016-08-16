# context-logging - pretty contextual key-value colored logging

## Overview

**context-logging** provides contextual (with key-value scheme), level-colored (optional) logger based on _logging_ module.

## Usage example

```python
import logging.config
from context_logging import getLogger


logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)-7s %(message)-20s %(context)s',
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
        },
    }
})
logger = getLogger(__name__, context='executor')
logger.critical('step1', value1=42)
logger.critical('step2', value2=8)
```
...will result in:

```
2016-08-07 23:17:07,348 CRITICAL step1                context="executor", value1=42
2016-08-07 23:17:07,348 CRITICAL step2                context="executor", value2=8
```

See sample.py for full example

## Features

 * **Context logger** - creating logger with pre-defined dict, that will appear in log messages
 * **Context log messages** - adding custom named args for each log messages in the same format
 * **Colored formatter** - paint each log level in appropriate colors (optionally)

## Run tests

```bash
python3 -m unittest discover tests
```
