# simple_flaky.py
import random
import time

def flaky_function(x: int) -> str:
    """Return 'ok' most of the time, but sometimes misbehaves."""
    # Random transient error
    if random.random() < 0.2:
        return "error"

    # Time-based nondeterminism: if system clock second is even, delay
    if time.localtime().tm_sec % 2 == 0:
        time.sleep(0.05)  # may cause timeout or race

    return f"processed-{x}"
