# -*- coding: utf-8 -*-

from module.plugins.internal.SimpleCrypter import SimpleCrypter, create_getInfo


class CrockoComFolder(SimpleCrypter):
    __name__    = "CrockoComFolder"
    __type__    = "crypter"
    __version__ = "0.01"

    __pattern__ = r'http://(?:www\.)?crocko\.com/f/.+'
    __config__  = [("use_subfolder", "bool", "Save package to subfolder", True),
                   ("subfolder_per_package", "bool", "Create a subfolder for each package", True)]

    __description__ = """Crocko.com folder decrypter plugin"""
    __license__     = "GPLv3"
    __authors__     = [("zoidberg", "zoidberg@mujmail.cz")]


    LINK_PATTERN = r'<td class="last"><a href="([^"]+)">download</a>'


getInfo = create_getInfo(CrockoComFolder)
