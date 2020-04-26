#
# Autogenerated by Thrift Compiler (0.7.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class Iface:
  def downloadMesh(self, name):
    """
    Parameters:
     - name
    """
    pass

  def downloadTexture(self, name, imageType, width, height):
    """
    Parameters:
     - name
     - imageType
     - width
     - height
    """
    pass

  def downloadGroup(self, name):
    """
    Parameters:
     - name
    """
    pass

  def query(self, dataPaths):
    """
    Parameters:
     - dataPaths
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def downloadMesh(self, name):
    """
    Parameters:
     - name
    """
    self.send_downloadMesh(name)
    return self.recv_downloadMesh()

  def send_downloadMesh(self, name):
    self._oprot.writeMessageBegin(b'downloadMesh', TMessageType.CALL, self._seqid)
    args = downloadMesh_args()
    args.name = name
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_downloadMesh(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = downloadMesh_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadMesh failed: unknown result");

  def downloadTexture(self, name, imageType, width, height):
    """
    Parameters:
     - name
     - imageType
     - width
     - height
    """
    self.send_downloadTexture(name, imageType, width, height)
    return self.recv_downloadTexture()

  def send_downloadTexture(self, name, imageType, width, height):
    self._oprot.writeMessageBegin(b'downloadTexture', TMessageType.CALL, self._seqid)
    args = downloadTexture_args()
    args.name = name
    args.imageType = imageType
    args.width = width
    args.height = height
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_downloadTexture(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = downloadTexture_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadTexture failed: unknown result");

  def downloadGroup(self, name):
    """
    Parameters:
     - name
    """
    self.send_downloadGroup(name)
    return self.recv_downloadGroup()

  def send_downloadGroup(self, name):
    self._oprot.writeMessageBegin(b'downloadGroup', TMessageType.CALL, self._seqid)
    args = downloadGroup_args()
    args.name = name
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_downloadGroup(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = downloadGroup_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "downloadGroup failed: unknown result");

  def query(self, dataPaths):
    """
    Parameters:
     - dataPaths
    """
    self.send_query(dataPaths)
    return self.recv_query()

  def send_query(self, dataPaths):
    self._oprot.writeMessageBegin(b'query', TMessageType.CALL, self._seqid)
    args = query_args()
    args.dataPaths = dataPaths
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_query(self, ):
    (fname, mtype, rseqid) = self._iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(self._iprot)
      self._iprot.readMessageEnd()
      raise x
    result = query_result()
    result.read(self._iprot)
    self._iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "query failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap[b"downloadMesh"] = Processor.process_downloadMesh
    self._processMap[b"downloadTexture"] = Processor.process_downloadTexture
    self._processMap[b"downloadGroup"] = Processor.process_downloadGroup
    self._processMap[b"query"] = Processor.process_query

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_downloadMesh(self, seqid, iprot, oprot):
    args = downloadMesh_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = downloadMesh_result()
    result.success = self._handler.downloadMesh(args.name)
    oprot.writeMessageBegin(b"downloadMesh", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_downloadTexture(self, seqid, iprot, oprot):
    args = downloadTexture_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = downloadTexture_result()
    result.success = self._handler.downloadTexture(args.name, args.imageType, args.width, args.height)
    oprot.writeMessageBegin(b"downloadTexture", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_downloadGroup(self, seqid, iprot, oprot):
    args = downloadGroup_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = downloadGroup_result()
    result.success = self._handler.downloadGroup(args.name)
    oprot.writeMessageBegin(b"downloadGroup", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_query(self, seqid, iprot, oprot):
    args = query_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = query_result()
    result.success = self._handler.query(args.dataPaths)
    oprot.writeMessageBegin(b"query", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class downloadMesh_args:
  """
  Attributes:
   - name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, b'name', None, None, ), # 1
  )

  def __init__(self, name=None,):
    self.name = name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'downloadMesh_args')
    if self.name is not None:
      oprot.writeFieldBegin(b'name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class downloadMesh_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.STRUCT, b'success', (Mesh, Mesh.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.STRUCT:
          self.success = Mesh()
          self.success.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'downloadMesh_result')
    if self.success is not None:
      oprot.writeFieldBegin(b'success', TType.STRUCT, 0)
      self.success.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class downloadTexture_args:
  """
  Attributes:
   - name
   - imageType
   - width
   - height
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, b'name', None, None, ), # 1
    (2, TType.I32, b'imageType', None, None, ), # 2
    (3, TType.I16, b'width', None, None, ), # 3
    (4, TType.I16, b'height', None, None, ), # 4
  )

  def __init__(self, name=None, imageType=None, width=None, height=None,):
    self.name = name
    self.imageType = imageType
    self.width = width
    self.height = height

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.imageType = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.width = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I16:
          self.height = iprot.readI16();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'downloadTexture_args')
    if self.name is not None:
      oprot.writeFieldBegin(b'name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.imageType is not None:
      oprot.writeFieldBegin(b'imageType', TType.I32, 2)
      oprot.writeI32(self.imageType)
      oprot.writeFieldEnd()
    if self.width is not None:
      oprot.writeFieldBegin(b'width', TType.I16, 3)
      oprot.writeI16(self.width)
      oprot.writeFieldEnd()
    if self.height is not None:
      oprot.writeFieldBegin(b'height', TType.I16, 4)
      oprot.writeI16(self.height)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class downloadTexture_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, b'success', (TType.STRING,None), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype24, _size21) = iprot.readListBegin()
          for _i25 in range(_size21):
            _elem26 = iprot.readString();
            self.success.append(_elem26)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'downloadTexture_result')
    if self.success is not None:
      oprot.writeFieldBegin(b'success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRING, len(self.success))
      for iter27 in self.success:
        oprot.writeString(iter27)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class downloadGroup_args:
  """
  Attributes:
   - name
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, b'name', None, None, ), # 1
  )

  def __init__(self, name=None,):
    self.name = name

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'downloadGroup_args')
    if self.name is not None:
      oprot.writeFieldBegin(b'name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class downloadGroup_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, b'success', (TType.STRING,None), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype31, _size28) = iprot.readListBegin()
          for _i32 in range(_size28):
            _elem33 = iprot.readString();
            self.success.append(_elem33)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'downloadGroup_result')
    if self.success is not None:
      oprot.writeFieldBegin(b'success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRING, len(self.success))
      for iter34 in self.success:
        oprot.writeString(iter34)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class query_args:
  """
  Attributes:
   - dataPaths
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, b'dataPaths', (TType.STRING,None), None, ), # 1
  )

  def __init__(self, dataPaths=None,):
    self.dataPaths = dataPaths

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.dataPaths = []
          (_etype38, _size35) = iprot.readListBegin()
          for _i39 in range(_size35):
            _elem40 = iprot.readString();
            self.dataPaths.append(_elem40)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'query_args')
    if self.dataPaths is not None:
      oprot.writeFieldBegin(b'dataPaths', TType.LIST, 1)
      oprot.writeListBegin(TType.STRING, len(self.dataPaths))
      for iter41 in self.dataPaths:
        oprot.writeString(iter41)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class query_result:
  """
  Attributes:
   - success
  """

  thrift_spec = (
    (0, TType.LIST, b'success', (TType.STRUCT,(Property, Property.thrift_spec)), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 0:
        if ftype == TType.LIST:
          self.success = []
          (_etype45, _size42) = iprot.readListBegin()
          for _i46 in range(_size42):
            _elem47 = Property()
            _elem47.read(iprot)
            self.success.append(_elem47)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin(b'query_result')
    if self.success is not None:
      oprot.writeFieldBegin(b'success', TType.LIST, 0)
      oprot.writeListBegin(TType.STRUCT, len(self.success))
      for iter48 in self.success:
        iter48.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
