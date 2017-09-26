#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Systems, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging

from pyswitch.RestDevice import RestDevice
from pyswitch.NetConfDevice import NetConfDevice
from pyswitch.SnmpCliDevice import SnmpCliDevice
from pyswitch.snmp.snmpconnector import SnmpConnector as SNMPDevice
from pyswitch.snmp.snmpconnector import SnmpUtils as SNMPUtils
from pyswitch.snmp.snmpconnector import SNMPError as SNMPError


class DeviceCommError(Exception):
    """
    Error with device communication.
    """
    pass


class Reply:

    def __init__(self, xml):
        self.data = xml


# pylint: disable=E1101
class Device(object):
    """
    Device object holds the state for a single NOS device.

    Attributes:
        bgp: BGP related actions and attributes.
        interface: Interface related actions and attributes.
        snmp: SNMP related actions and attributes.
        lldp: LLDP related actions and attributes.
        system: System level actions and attributes.
    """

    def __init__(self, **kwargs):
        """

        """
        kwargs['base'] = self
        self.connection_type = kwargs.get('connection_type', 'REST')

        conn = kwargs.get('conn')
        host = conn[0]
        snmpport = kwargs.get('snmpport', 161)
        snmpver = kwargs.get('snmpver', 2)
        snmpv2c = kwargs.get('snmpv2c', 'public')

        sysobj = ''

        try:
           snmpdev = SNMPDevice(host=host, port=snmpport, version=snmpver, community=snmpv2c)
           sysobj = str(snmpdev.get("1.3.6.1.2.1.1.2.0"))
        except (SNMPError) as error:
           logging.error(error)
           #print "SNMP query failed for device: ", error

        if sysobj in SNMPUtils.SNMP_DEVICE_MAP:
            if SNMPUtils.SNMP_DEVICE_MAP[sysobj] == 'MLX':
                self.connection_type = 'SNMPCLI'

        if self.connection_type is 'SNMPCLI':
            self.device_type = SnmpCliDevice(sysobj, **kwargs)
        if self.connection_type is 'REST':
            self.device_type = RestDevice(**kwargs)
        elif self.connection_type is 'NETCONF':
            self.device_type = NetConfDevice(**kwargs)

    def __enter__(self):
        self.device_type.__enter__()
        return self

    def __exit__(self, exctype, excisnt, exctb):
        return self.device_type.__exit__(exctype, excisnt, exctb)

    @property
    def asset(self):
        return self.device_type._mgr

    @property
    def mac_table(self):
        return self.device_type.mac_table

    @property
    def os_type(self):
        return self.device_type.os_type

    @property
    def suports_rbridge(self):
        return self.device_type.suports_rbridge

    @property
    def firmware_version(self):
        return self.device_type.firmware_version

    def _callback_main(self, call, handler='edit_config', target='running',
                       source='startup'):
        return self.device_type.__callback_main(self, call, handler, target, source)

    def reconnect(self):
        return self.device_type.reconnect()

    def find_interface_by_mac(self, **kwargs):
        return self.device_type.find_interface_by_mac(**kwargs)

    def close(self):
        return self.device_type.close()
