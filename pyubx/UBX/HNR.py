from pyubx.UBXMessage import UBXMessage, initMessageClass, addGet
import struct
from pyubx.Types import U1, U2, U4, X2, X4, U, I2, I4, X1

@initMessageClass
class HNR:
    """Message class NAV."""

    _class = 0x28
    # class PVT_GET:
    #
    #     _id = 0x00
    #
    #     class Fields:
    #         iTow = U4(1)

    @addGet
    class PVT:

        _id = 0x00

        class Fields:

            iTOW = U4(1)
            year =  U2(2)
            month = U1(3)
            day = U1(4)
            hour = U1(5)
            min = U1(6)
            sec = U1(7)
            valid = X1(8)
            nano = I4(9)
            gpsFix = U1(10)
            flags = X1(11)
            reserved1 = U2(12)
            lon = I4(13)
            lat = I4(14)
            height = I4(15)
            hMSL = I4(16)
            gSpeed = I4(17)
            headMot = I4(18)
            headVeh = I4(19)
            hAcc = U4(20)
            vAcc = U4(21)
            sAcc = U4(22)
            headAcc = U4(23)
            reserved2 = U4(24)
