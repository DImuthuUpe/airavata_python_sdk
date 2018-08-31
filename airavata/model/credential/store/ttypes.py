#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class CredentialOwnerType(object):
    GATEWAY = 0
    USER = 1

    _VALUES_TO_NAMES = {
        0: "GATEWAY",
        1: "USER",
    }

    _NAMES_TO_VALUES = {
        "GATEWAY": 0,
        "USER": 1,
    }


class SummaryType(object):
    """
    Data Types supported in Airavata. The primitive data types

    """
    SSH = 0
    PASSWD = 1
    CERT = 2

    _VALUES_TO_NAMES = {
        0: "SSH",
        1: "PASSWD",
        2: "CERT",
    }

    _NAMES_TO_VALUES = {
        "SSH": 0,
        "PASSWD": 1,
        "CERT": 2,
    }


class SSHCredential(object):
    """
    Attributes:
     - gatewayId
     - username
     - passphrase
     - publicKey
     - privateKey
     - persistedTime
     - token
     - description
     - credentialOwnerType
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'username', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'passphrase', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'publicKey', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'privateKey', 'UTF8', None, ),  # 5
        (6, TType.I64, 'persistedTime', None, None, ),  # 6
        (7, TType.STRING, 'token', 'UTF8', None, ),  # 7
        (8, TType.STRING, 'description', 'UTF8', None, ),  # 8
        (9, TType.I32, 'credentialOwnerType', None, 0, ),  # 9
    )

    def __init__(self, gatewayId=None, username=None, passphrase=None, publicKey=None, privateKey=None, persistedTime=None, token=None, description=None, credentialOwnerType=thrift_spec[9][4],):
        self.gatewayId = gatewayId
        self.username = username
        self.passphrase = passphrase
        self.publicKey = publicKey
        self.privateKey = privateKey
        self.persistedTime = persistedTime
        self.token = token
        self.description = description
        self.credentialOwnerType = credentialOwnerType

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.passphrase = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.publicKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.privateKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.persistedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.credentialOwnerType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('SSHCredential')
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 1)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 2)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.passphrase is not None:
            oprot.writeFieldBegin('passphrase', TType.STRING, 3)
            oprot.writeString(self.passphrase.encode('utf-8') if sys.version_info[0] == 2 else self.passphrase)
            oprot.writeFieldEnd()
        if self.publicKey is not None:
            oprot.writeFieldBegin('publicKey', TType.STRING, 4)
            oprot.writeString(self.publicKey.encode('utf-8') if sys.version_info[0] == 2 else self.publicKey)
            oprot.writeFieldEnd()
        if self.privateKey is not None:
            oprot.writeFieldBegin('privateKey', TType.STRING, 5)
            oprot.writeString(self.privateKey.encode('utf-8') if sys.version_info[0] == 2 else self.privateKey)
            oprot.writeFieldEnd()
        if self.persistedTime is not None:
            oprot.writeFieldBegin('persistedTime', TType.I64, 6)
            oprot.writeI64(self.persistedTime)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 7)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 8)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        if self.credentialOwnerType is not None:
            oprot.writeFieldBegin('credentialOwnerType', TType.I32, 9)
            oprot.writeI32(self.credentialOwnerType)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        if self.username is None:
            raise TProtocolException(message='Required field username is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CredentialSummary(object):
    """
    Attributes:
     - type
     - gatewayId
     - username
     - publicKey
     - persistedTime
     - token
     - description
    """

    thrift_spec = (
        None,  # 0
        (1, TType.I32, 'type', None, None, ),  # 1
        (2, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'username', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'publicKey', 'UTF8', None, ),  # 4
        (5, TType.I64, 'persistedTime', None, None, ),  # 5
        (6, TType.STRING, 'token', 'UTF8', None, ),  # 6
        (7, TType.STRING, 'description', 'UTF8', None, ),  # 7
    )

    def __init__(self, type=None, gatewayId=None, username=None, publicKey=None, persistedTime=None, token=None, description=None,):
        self.type = type
        self.gatewayId = gatewayId
        self.username = username
        self.publicKey = publicKey
        self.persistedTime = persistedTime
        self.token = token
        self.description = description

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.type = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.publicKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.persistedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CredentialSummary')
        if self.type is not None:
            oprot.writeFieldBegin('type', TType.I32, 1)
            oprot.writeI32(self.type)
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 2)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 3)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.publicKey is not None:
            oprot.writeFieldBegin('publicKey', TType.STRING, 4)
            oprot.writeString(self.publicKey.encode('utf-8') if sys.version_info[0] == 2 else self.publicKey)
            oprot.writeFieldEnd()
        if self.persistedTime is not None:
            oprot.writeFieldBegin('persistedTime', TType.I64, 5)
            oprot.writeI64(self.persistedTime)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 6)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 7)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.type is None:
            raise TProtocolException(message='Required field type is unset!')
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        if self.username is None:
            raise TProtocolException(message='Required field username is unset!')
        if self.token is None:
            raise TProtocolException(message='Required field token is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CommunityUser(object):
    """
    Attributes:
     - gatewayName
     - username
     - userEmail
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'gatewayName', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'username', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'userEmail', 'UTF8', None, ),  # 3
    )

    def __init__(self, gatewayName=None, username=None, userEmail=None,):
        self.gatewayName = gatewayName
        self.username = username
        self.userEmail = userEmail

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.gatewayName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.username = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.userEmail = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CommunityUser')
        if self.gatewayName is not None:
            oprot.writeFieldBegin('gatewayName', TType.STRING, 1)
            oprot.writeString(self.gatewayName.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayName)
            oprot.writeFieldEnd()
        if self.username is not None:
            oprot.writeFieldBegin('username', TType.STRING, 2)
            oprot.writeString(self.username.encode('utf-8') if sys.version_info[0] == 2 else self.username)
            oprot.writeFieldEnd()
        if self.userEmail is not None:
            oprot.writeFieldBegin('userEmail', TType.STRING, 3)
            oprot.writeString(self.userEmail.encode('utf-8') if sys.version_info[0] == 2 else self.userEmail)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.gatewayName is None:
            raise TProtocolException(message='Required field gatewayName is unset!')
        if self.username is None:
            raise TProtocolException(message='Required field username is unset!')
        if self.userEmail is None:
            raise TProtocolException(message='Required field userEmail is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class CertificateCredential(object):
    """
    Attributes:
     - communityUser
     - x509Cert
     - notAfter
     - privateKey
     - lifeTime
     - notBefore
     - persistedTime
     - token
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'communityUser', (CommunityUser, CommunityUser.thrift_spec), None, ),  # 1
        (2, TType.STRING, 'x509Cert', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'notAfter', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'privateKey', 'UTF8', None, ),  # 4
        (5, TType.I64, 'lifeTime', None, None, ),  # 5
        (6, TType.STRING, 'notBefore', 'UTF8', None, ),  # 6
        (7, TType.I64, 'persistedTime', None, None, ),  # 7
        (8, TType.STRING, 'token', 'UTF8', None, ),  # 8
    )

    def __init__(self, communityUser=None, x509Cert=None, notAfter=None, privateKey=None, lifeTime=None, notBefore=None, persistedTime=None, token=None,):
        self.communityUser = communityUser
        self.x509Cert = x509Cert
        self.notAfter = notAfter
        self.privateKey = privateKey
        self.lifeTime = lifeTime
        self.notBefore = notBefore
        self.persistedTime = persistedTime
        self.token = token

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.communityUser = CommunityUser()
                    self.communityUser.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.x509Cert = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.notAfter = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.privateKey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.lifeTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.notBefore = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.persistedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('CertificateCredential')
        if self.communityUser is not None:
            oprot.writeFieldBegin('communityUser', TType.STRUCT, 1)
            self.communityUser.write(oprot)
            oprot.writeFieldEnd()
        if self.x509Cert is not None:
            oprot.writeFieldBegin('x509Cert', TType.STRING, 2)
            oprot.writeString(self.x509Cert.encode('utf-8') if sys.version_info[0] == 2 else self.x509Cert)
            oprot.writeFieldEnd()
        if self.notAfter is not None:
            oprot.writeFieldBegin('notAfter', TType.STRING, 3)
            oprot.writeString(self.notAfter.encode('utf-8') if sys.version_info[0] == 2 else self.notAfter)
            oprot.writeFieldEnd()
        if self.privateKey is not None:
            oprot.writeFieldBegin('privateKey', TType.STRING, 4)
            oprot.writeString(self.privateKey.encode('utf-8') if sys.version_info[0] == 2 else self.privateKey)
            oprot.writeFieldEnd()
        if self.lifeTime is not None:
            oprot.writeFieldBegin('lifeTime', TType.I64, 5)
            oprot.writeI64(self.lifeTime)
            oprot.writeFieldEnd()
        if self.notBefore is not None:
            oprot.writeFieldBegin('notBefore', TType.STRING, 6)
            oprot.writeString(self.notBefore.encode('utf-8') if sys.version_info[0] == 2 else self.notBefore)
            oprot.writeFieldEnd()
        if self.persistedTime is not None:
            oprot.writeFieldBegin('persistedTime', TType.I64, 7)
            oprot.writeI64(self.persistedTime)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 8)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.communityUser is None:
            raise TProtocolException(message='Required field communityUser is unset!')
        if self.x509Cert is None:
            raise TProtocolException(message='Required field x509Cert is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class PasswordCredential(object):
    """
    Attributes:
     - gatewayId
     - portalUserName
     - loginUserName
     - password
     - description
     - persistedTime
     - token
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'portalUserName', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'loginUserName', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'password', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'description', 'UTF8', None, ),  # 5
        (6, TType.I64, 'persistedTime', None, None, ),  # 6
        (7, TType.STRING, 'token', 'UTF8', None, ),  # 7
    )

    def __init__(self, gatewayId=None, portalUserName=None, loginUserName=None, password=None, description=None, persistedTime=None, token=None,):
        self.gatewayId = gatewayId
        self.portalUserName = portalUserName
        self.loginUserName = loginUserName
        self.password = password
        self.description = description
        self.persistedTime = persistedTime
        self.token = token

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.portalUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.loginUserName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.password = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.description = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.persistedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.token = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('PasswordCredential')
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 1)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.portalUserName is not None:
            oprot.writeFieldBegin('portalUserName', TType.STRING, 2)
            oprot.writeString(self.portalUserName.encode('utf-8') if sys.version_info[0] == 2 else self.portalUserName)
            oprot.writeFieldEnd()
        if self.loginUserName is not None:
            oprot.writeFieldBegin('loginUserName', TType.STRING, 3)
            oprot.writeString(self.loginUserName.encode('utf-8') if sys.version_info[0] == 2 else self.loginUserName)
            oprot.writeFieldEnd()
        if self.password is not None:
            oprot.writeFieldBegin('password', TType.STRING, 4)
            oprot.writeString(self.password.encode('utf-8') if sys.version_info[0] == 2 else self.password)
            oprot.writeFieldEnd()
        if self.description is not None:
            oprot.writeFieldBegin('description', TType.STRING, 5)
            oprot.writeString(self.description.encode('utf-8') if sys.version_info[0] == 2 else self.description)
            oprot.writeFieldEnd()
        if self.persistedTime is not None:
            oprot.writeFieldBegin('persistedTime', TType.I64, 6)
            oprot.writeI64(self.persistedTime)
            oprot.writeFieldEnd()
        if self.token is not None:
            oprot.writeFieldBegin('token', TType.STRING, 7)
            oprot.writeString(self.token.encode('utf-8') if sys.version_info[0] == 2 else self.token)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.gatewayId is None:
            raise TProtocolException(message='Required field gatewayId is unset!')
        if self.portalUserName is None:
            raise TProtocolException(message='Required field portalUserName is unset!')
        if self.loginUserName is None:
            raise TProtocolException(message='Required field loginUserName is unset!')
        if self.password is None:
            raise TProtocolException(message='Required field password is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
