# Converting Tuple to Hex with unknown type
realVal = struct.unpack( "&lt;" + evalType, ( rawVal ) )[0].hex()
