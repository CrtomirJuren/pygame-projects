# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:57:53 2020

@author: crtjur
"""

"""
$ python
Python 2.7.13 (default, Apr  4 2017, 08:47:57)
[GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> from simple_device import SimpleDevice
>>> device = SimpleDevice()
Processing current state: LockedState
>>> 
>>> device.on_event('device_locked')
>>> device.on_event('pin_entered')
Processing current state: UnlockedState
>>> 
>>> device.state
UnlockedState
>>> 
>>> device.on_event('device_locked')
Processing current state: LockedState
>>> 
>>> device.state
LockedState
>>> device.on_event('device_locked')
"""