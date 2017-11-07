

class SnmpMib:
    """
    Class containing all the standard SNMP MIBs supported by Pyswitch
    """
    mib_oid_map = {
        'sysObjectId': '1.3.6.1.2.1.1.2.0',
        'dot1qVlanStaticTable': '1.3.6.1.2.1.17.7.1.4.3.1',
        'dot1qVlanStaticEntry': '1.3.6.1.2.1.17.7.1.4.3.1.1',
        'dot1qVlanStaticName': '1.3.6.1.2.1.17.7.1.4.3.1.2',
        'dot1qVlanStaticEgressPorts': '1.3.6.1.2.1.17.7.1.4.3.1.2',
        'dot1qVlanStaticUntaggedPorts': '1.3.6.1.2.1.17.7.1.4.3.1.4',
        'dot1qVlanStaticRowStatus': '1.3.6.1.2.1.17.7.1.4.3.1.5',
        'dot3adAggTable': '1.2.840.10006.300.43.1.1.1.1',
        'dot3adAggIndex': '1.2.840.10006.300.43.1.1.1.1.1',
        'dot3adAggMACAddress': '1.2.840.10006.300.43.1.1.1.1.2',
        'dot3adAggActorSystemPriority': '1.2.840.10006.300.43.1.1.1.1.3',
        'dot3adAggActorSystemID': '1.2.840.10006.300.43.1.1.1.1.4',
        'dot3adAggAggregateOrIndividual': '1.2.840.10006.300.43.1.1.1.1.5',
        'dot3adAggActorAdminKey': '1.2.840.10006.300.43.1.1.1.1.6',
        'dot3adAggActorOperKey': '1.2.840.10006.300.43.1.1.1.1.7',
        'dot3adAggPartnerSystemID': '1.2.840.10006.300.43.1.1.1.1.8',
        'dot3adAggPartnerSystemPriority': '1.2.840.10006.300.43.1.1.1.1.9',
        'dot3adAggPartnerOperKey': '1.2.840.10006.300.43.1.1.1.1.10',
        'dot3adAggCollectorMaxDelay': '1.2.840.10006.300.43.1.1.1.1.11',
        'ifXTable': '1.3.6.1.2.1.31.1.1',
        'ifXEntry': '1.3.6.1.2.1.31.1.1.1',
        'ifAdminStatus': '1.3.6.1.2.1.2.2.1.7',
        'ifAlias': '1.3.6.1.2.1.31.1.1.1.18',
        'snRtIpPortIfMtu': '1.3.6.1.4.1.1991.1.2.2.20.1.2',
        'ipv6IfEffectiveMtu': '1.3.6.1.2.1.55.1.5.1.4',
        'ipNetToPhysicalTable': '1.3.6.1.2.1.4.35',
        'ipNetToPhysicalEntry': '1.3.6.1.2.1.4.35.1',
        'ipNetToPhysicalIfindex': '1.3.6.1.2.1.4.35.1.1',
        'ipNetToPhysicalNetAddressType': '1.3.6.1.2.1.4.35.1.2',
        'ipNetToPhysicalNetAddress': '1.3.6.1.2.1.4.35.1.3',
        'ipNetToPhysicalPhyAddress': '1.3.6.1.2.1.4.35.1.4',
        'ipNetToPhysicalLastUpdated': '1.3.6.1.2.1.4.35.1.5',
        'ipNetToPhysicalType': '1.3.6.1.2.1.4.35.1.6',
        'ipNetToPhysicalState': '1.3.6.1.2.1.4.35.1.7',
        'ipNetToPhysicalRowStatus': '1.3.6.1.2.1.4.35.1.8',
    }
