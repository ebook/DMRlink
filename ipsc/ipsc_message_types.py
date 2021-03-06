# Copyright (c) 2013 Cortney T. Buffington, N0MJS and the K0USY Group. n0mjs@me.com
#
# This work is licensed under the Creative Commons Attribution-ShareAlike
# 3.0 Unported License.To view a copy of this license, visit
# http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to
# Creative Commons, 444 Castro Street, Suite 900, Mountain View,
# California, 94041, USA.

# Known IPSC Message Types
CALL_CONFIRMATION     = '\x05' # Confirmation FROM the recipient of a confirmed call.
CALL_MON_ORIGIN       = '\x61' #  |
CALL_MON_RPT          = '\x62' #  | Exact meaning unknown
CALL_MON_NACK         = '\x63' #  |
XCMP_XNL              = '\x70' # XCMP/XNL control message
GROUP_VOICE           = '\x80'
PVT_VOICE             = '\x81'
GROUP_DATA            = '\x83'
PVT_DATA              = '\x84'
RPT_WAKE_UP           = '\x85' # Similar to OTA DMR "wake up"
MASTER_REG_REQ        = '\x90' # FROM peer TO master
MASTER_REG_REPLY      = '\x91' # FROM master TO peer
PEER_LIST_REQ         = '\x92'
PEER_LIST_REPLY       = '\x93'
PEER_REG_REQ          = '\x94' # Peer registration request
PEER_REG_REPLY        = '\x95' # Peer registration reply
MASTER_ALIVE_REQ      = '\x96' # FROM peer TO master
MASTER_ALIVE_REPLY    = '\x97' # FROM master TO peer
PEER_ALIVE_REQ        = '\x98' # Peer keep alive request
PEER_ALIVE_REPLY      = '\x99' # Peer keep alive reply
DE_REG_REQ            = '\x9A' # Request de-registration from system
DE_REG_REPLY          = '\x9B' # De-registration reply

# IPSC Version Information
IPSC_VER_14           = '\x00'
IPSC_VER_15           = '\x00'
IPSC_VER_15A          = '\x00'
IPSC_VER_16           = '\x01'
IPSC_VER_17           = '\x02'
IPSC_VER_18           = '\x02'
IPSC_VER_19           = '\x03'
IPSC_VER_22           = '\x04'

# Link Type Values - assumed that cap+, etc. are different, this is all I can confirm
LINK_TYPE_IPSC        = '\x04'

# IPSC Version and Link Type are Used for a 4-byte version field in registration packets
IPSC_VER              = LINK_TYPE_IPSC + IPSC_VER_19 + LINK_TYPE_IPSC + IPSC_VER_17

# Packets that must originate from a peer (or master peer)
ANY_PEER_REQUIRED = [GROUP_VOICE, PVT_VOICE, GROUP_DATA, PVT_DATA, CALL_MON_ORIGIN, CALL_MON_RPT, CALL_MON_NACK, XCMP_XNL, RPT_WAKE_UP, DE_REG_REQ]

# Packets that must originate from a non-master peer
PEER_REQUIRED = [PEER_ALIVE_REQ, PEER_ALIVE_REPLY, PEER_REG_REQ, PEER_REG_REPLY]

# Packets that must originate from a master peer
MASTER_REQUIRED = [PEER_LIST_REPLY, MASTER_ALIVE_REPLY]

# User-Generated Packet Types
USER_PACKETS = [GROUP_VOICE, PVT_VOICE, GROUP_DATA, PVT_DATA]

# Conditions for accepting certain types of messages... the cornerstone of a secure IPSC system :)
'''
REQ_VALID_PEER = [
    PEER_REG_REQ,
    PEER_REG_REPLY
]

REQ_VALID_MASTER = [
    MASTER_REG_REQ,
    MASTER_REG_REPLY
]

REQ_MASTER_CONNECTED = [
    CALL_MON_ORIGIN,
    CALL_MON_RPT,
    CALL_MON_NACK,
    XCMP_XNL,
    GROUP_VOICE,
    PVT_VOICE,
    GROUP_DATA,
    GROUP_VOICE,
    PVT_DATA,
    RPT_WAKE_UP,
    MASTER_ALIVE_REQ,
    MASTER_ALIVE_REPLY,
    DE_REG_REQ,
    DE_REG_REPLY 
]

REQ_PEER_CONNECTED = [
    PEER_ALIVE_REQ,
    PEER_ALIVE_REPLY
]

REQ_VALID_MASTER_OR_PEER = [
    REQ_VALID_PEER, REQ_VALID_MASTER
]
'''