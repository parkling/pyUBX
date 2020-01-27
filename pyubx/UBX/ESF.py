"""External Sensor Fusion Messages:
https://www.u-blox.com/en/docs/UBX-13003221#page=259&zoom=160,-87,770
"""
#UBX.ESF.RAW.Get().serialize()
#b'\xb5b\x10\x03\x00\x00\x13I'

from pyubx.UBXMessage import initMessageClass, addGet
from pyubx.Types import X4, U4, X2, U2


@initMessageClass
class ESF:
    """Message class ESF."""

    _class = 0x10

    @addGet
    class RAW:

        _id = 0x03

        class Fields:
            reserved1 = U4(1)#U1(1,4)  works with either U4 or U1(1,4)

            class Repeated:
                data = X4(1)
                sTtag = U4(2)

    @addGet
    class MEAS:
        _id = 0x02

        class Fields:
            timeTag = U4(1)  # U1(1,4)  works with either U4 or U1(1,4)
            flags = X2(2)
            id = U2(3)

            class Repeated:
                data = X4(1)
                calibTtag = U4(2)

