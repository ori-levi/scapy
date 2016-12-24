"""
HTTP: Hypertext Transfer Protocol.
"""

__author__ = 'Ori Levi (ori1991@gmail.com)'

from scapy.packet import Packet
from scapy.fields import StrField, Field


class HTTP(Packet):
    """
    GET / HTTP/1.1
    Header: va;ie
    """

    name = "HTTP"
    fields_desc = [
        StrField('method', ''),
        StrField('version', ''),
        StrField('path', ''),
        StrField('query', ''),
        StrField('body', ''),
        StrField('headers', '')
    ]
