from . import timework as tw

import time
from random import randint


@tw.timer(print, detail=True)
def timer_demo_a(s):
    """
    output example:
      [TIMEWORK] Start:  Mon Feb  8 03:35:06 2021
      [TIMEWORK] Finish: Mon Feb  8 03:35:08 2021
      [TIMEWORK] timer_demo_a used: 00:00:02.406
    """
    time.sleep(s)
    return s * 2


@tw.timer(timeout=1)
def timer_demo_b(m):
    """
    if not timeout:
      work as normal
    If timed out:
      raise TimeError
      e.result = return_code
      e.detail = time_used
    """
    i = 0
    while i < 2 ** m:
        i += 1
    return i


@tw.limit(3)
def limit_demo(m):
    """
    if not timeout:
      work as normal
    If timed out:
      raise TimeError
    """
    i = 0
    while i < 2 ** m:
        i += 1
    return i


def test_timer():
    for _ in range(10):
        d = randint(10, 25)
        x = timer_demo_a(d / 10)
        assert x == 2 * d

    for _ in range(10):
        d = randint(10, 25)
        try:
            rc = timer_demo_b(d)
        except tw.TimeError as e:
            assert e.message.startswith('[TIMEWORK] timer_demo_b')
            assert e.result == 2 ** d
            assert e.detail > 1
        else:
            assert rc == 2 ** d


def test_limit():
    for _ in range(10):
        d = randint(15, 35)
        try:
            rc = limit_demo(d)
        except tw.TimeError as e:
            assert e.message.startswith('[TIMEWORK] limit_demo')
            assert e.result is None
            assert e.detail is None
        else:
            assert rc == 2 ** d


def test_errors():
    try:
        timer_demo_b('string')
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        limit_demo('string')
    except Exception as e:
        assert isinstance(e, TypeError)
