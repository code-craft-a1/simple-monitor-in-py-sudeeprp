
from time import sleep
import sys


def catch_attention():
  for i in range(6):
    print('\r* ', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)


def check_range(value, min_val, max_val, message):
  if value < min_val or value > max_val:
    print(message)
    catch_attention()
    return False
  return True

def check_min(value, min_val, message):
  if value < min_val:
    print(message)
    catch_attention()
    return False
  return True

def vitals_ok(temperature, pulseRate, spo2):
  checks = [
    (check_range, (temperature, 95, 102, 'Temperature critical!')),
    (check_range, (pulseRate, 60, 100, 'Pulse Rate is out of range!')),
    (check_min, (spo2, 90, 'Oxygen Saturation out of range!'))
  ]
  for func, args in checks:
    if not func(*args):
      return False
  return True
