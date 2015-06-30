# -*- coding: utf-8 -*-
"""The Virtual File System (VFS) definitions."""

# The compression method definitions.
COMPRESSION_METHOD_BZIP2 = u'bzip2'
COMPRESSION_METHOD_DEFLATE = u'deflate'
COMPRESSION_METHOD_ZLIB = u'zlib'

# The encoding method definitions.
ENCODING_METHOD_BASE16 = u'base16'
ENCODING_METHOD_BASE32 = u'base32'
ENCODING_METHOD_BASE64 = u'base64'

# The type indicator definitions.
TYPE_INDICATOR_BDE = u'BDE'
TYPE_INDICATOR_BZIP2 = u'BZIP2'
TYPE_INDICATOR_COMPRESSED_STREAM = u'COMPRESSED_STREAM'
TYPE_INDICATOR_DATA_RANGE = u'DATA_RANGE'
TYPE_INDICATOR_ENCODED_STREAM = u'ENCODED_STREAM'
TYPE_INDICATOR_EWF = u'EWF'
TYPE_INDICATOR_FAKE = u'FAKE'
TYPE_INDICATOR_GZIP = u'GZIP'
TYPE_INDICATOR_MOUNT = u'MOUNT'
TYPE_INDICATOR_OS = u'OS'
TYPE_INDICATOR_QCOW = u'QCOW'
TYPE_INDICATOR_RAW = u'RAW'
TYPE_INDICATOR_SQLITE_BLOB = u'SQLITE_BLOB'
TYPE_INDICATOR_TAR = u'TAR'
TYPE_INDICATOR_TSK = u'TSK'
TYPE_INDICATOR_TSK_PARTITION = u'TSK_PARTITION'
TYPE_INDICATOR_VHDI = u'VHDI'
TYPE_INDICATOR_VMDK = u'VMDK'
TYPE_INDICATOR_VSHADOW = u'VSHADOW'
TYPE_INDICATOR_ZIP = u'ZIP'

ENCRYPTED_VOLUME_TYPE_INDICATORS = frozenset([
    TYPE_INDICATOR_BDE])

FILE_SYSTEM_TYPE_INDICATORS = frozenset([
    TYPE_INDICATOR_TSK])

STORAGE_MEDIA_IMAGE_TYPE_INDICATORS = frozenset([
    TYPE_INDICATOR_EWF,
    TYPE_INDICATOR_QCOW,
    TYPE_INDICATOR_RAW,
    TYPE_INDICATOR_VHDI,
    TYPE_INDICATOR_VMDK])

VOLUME_SYSTEM_TYPE_INDICATORS = frozenset([
    TYPE_INDICATOR_TSK_PARTITION,
    TYPE_INDICATOR_VSHADOW])

# The file entry types.
FILE_ENTRY_TYPE_DEVICE = 1
FILE_ENTRY_TYPE_DIRECTORY = 2
FILE_ENTRY_TYPE_FILE = 3
FILE_ENTRY_TYPE_LINK = 4
FILE_ENTRY_TYPE_SOCKET = 5
FILE_ENTRY_TYPE_PIPE = 6

# The format category definitions.
FORMAT_CATEGORY_UNDEFINED = 0
FORMAT_CATEGORY_ARCHIVE = 1
FORMAT_CATEGORY_COMPRESSED_STREAM = 2
FORMAT_CATEGORY_ENCODED_STREAM = 3
FORMAT_CATEGORY_FILE_SYSTEM = 4
FORMAT_CATEGORY_STORAGE_MEDIA_IMAGE = 5
FORMAT_CATEGORY_VOLUME_SYSTEM = 6
