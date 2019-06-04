# This file is executed on every boot (including wake-boot from deepsleep)
try:
  import usocket as socket
except:
  import socket

import esp

esp.osdebug(None)

import uos, machine
from machine import Pin

#uos.dupterm(None, 1) # disable REPL on UART(0)

import gc

import webrepl

webrepl.start()

gc.collect()