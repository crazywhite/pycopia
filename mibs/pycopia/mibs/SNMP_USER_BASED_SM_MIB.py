# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, snmpModules, Counter32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION, TestAndIncr, RowStatus, RowPointer, StorageType, AutonomousType
from SNMP_FRAMEWORK_MIB import SnmpAdminString, SnmpEngineID, snmpAuthProtocols, snmpPrivProtocols

class SNMP_USER_BASED_SM_MIB(ModuleObject):
	path = '/usr/share/mibs/ietf/SNMP-USER-BASED-SM-MIB'
	conformance = 5
	name = 'SNMP-USER-BASED-SM-MIB'
	language = 2
	description = 'The management information definitions for the\nSNMP User-based Security Model.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3414;\nsee the RFC itself for full legal notices.'

# nodes
class usmNoAuthProtocol(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 10, 1, 1, 1])
	name = 'usmNoAuthProtocol'

class usmHMACMD5AuthProtocol(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 10, 1, 1, 2])
	name = 'usmHMACMD5AuthProtocol'

class usmHMACSHAAuthProtocol(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 10, 1, 1, 3])
	name = 'usmHMACSHAAuthProtocol'

class usmNoPrivProtocol(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 10, 1, 2, 1])
	name = 'usmNoPrivProtocol'

class usmDESPrivProtocol(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 10, 1, 2, 2])
	name = 'usmDESPrivProtocol'

class snmpUsmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15])
	name = 'snmpUsmMIB'

class usmMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1])
	name = 'usmMIBObjects'

class usmStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1])
	name = 'usmStats'

class usmUser(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2])
	name = 'usmUser'

class usmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 2])
	name = 'usmMIBConformance'

class usmMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 2, 1])
	name = 'usmMIBCompliances'

class usmMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 2, 2])
	name = 'usmMIBGroups'


# macros
# types 

class KeyChange(pycopia.SMI.Basetypes.OctetString):
	status = 1

# scalars 
class usmStatsUnsupportedSecLevels(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usmStatsNotInTimeWindows(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usmStatsUnknownUserNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usmStatsUnknownEngineIDs(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usmStatsWrongDigests(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usmStatsDecryptionErrors(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usmUserSpinLock(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.TestAndIncr


# columns
class usmUserEngineID(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 1])
	syntaxobject = SnmpEngineID


class usmUserName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 2])
	syntaxobject = SnmpAdminString


class usmUserSecurityName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3])
	syntaxobject = SnmpAdminString


class usmUserCloneFrom(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class usmUserAuthProtocol(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class usmUserAuthKeyChange(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6])
	syntaxobject = KeyChange


class usmUserOwnAuthKeyChange(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7])
	syntaxobject = KeyChange


class usmUserPrivProtocol(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.AutonomousType


class usmUserPrivKeyChange(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9])
	syntaxobject = KeyChange


class usmUserOwnPrivKeyChange(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10])
	syntaxobject = KeyChange


class usmUserPublic(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class usmUserStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class usmUserStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class usmUserEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([usmUserEngineID, usmUserName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1])
	access = 2
	rowstatus = usmUserStatus
	columns = {'usmUserEngineID': usmUserEngineID, 'usmUserName': usmUserName, 'usmUserSecurityName': usmUserSecurityName, 'usmUserCloneFrom': usmUserCloneFrom, 'usmUserAuthProtocol': usmUserAuthProtocol, 'usmUserAuthKeyChange': usmUserAuthKeyChange, 'usmUserOwnAuthKeyChange': usmUserOwnAuthKeyChange, 'usmUserPrivProtocol': usmUserPrivProtocol, 'usmUserPrivKeyChange': usmUserPrivKeyChange, 'usmUserOwnPrivKeyChange': usmUserOwnPrivKeyChange, 'usmUserPublic': usmUserPublic, 'usmUserStorageType': usmUserStorageType, 'usmUserStatus': usmUserStatus}


# notifications (traps) 
# groups 
class usmMIBBasicGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 15, 2, 2, 1])
	group = [usmStatsUnsupportedSecLevels, usmStatsNotInTimeWindows, usmStatsUnknownUserNames, usmStatsUnknownEngineIDs, usmStatsWrongDigests, usmStatsDecryptionErrors, usmUserSpinLock, usmUserSecurityName, usmUserCloneFrom, usmUserAuthProtocol, usmUserAuthKeyChange, usmUserOwnAuthKeyChange, usmUserPrivProtocol, usmUserPrivKeyChange, usmUserOwnPrivKeyChange, usmUserPublic, usmUserStorageType, usmUserStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
