"""External Sensor Fusion Messages:
https://www.u-blox.com/en/docs/UBX-13003221#page=259&zoom=160,-87,770
"""
#UBX.ESF.RAW.Get().serialize()
#b'\xb5b\x10\x03\x00\x00\x13I'

from UBXMessage import initMessageClass, addGet
from Types import U,  U4,  X4


@initMessageClass
class ESF:
    """Message class ESF."""

    _class = 0x10

    @addGet
    class RAW:

        _id = 0x03

        class Fields:
            reserved1 = U(1,4)

            class Repeated:
                data = X4(1)
                sTtag = U4(2)

