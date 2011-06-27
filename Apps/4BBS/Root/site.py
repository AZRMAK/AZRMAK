#_*_ coding:utf-8 _*_

from quixote import get_request
from quixote.directory import Directory
from quixote import get_field
import MySQLdb

from Template import Template
from kind import KindDirectory

class RootDirectory (Directory):
    _q_exports = ["","kind"]
    def _q_index(self):       
        return Template.HTML % ("4BBS","Hello,4BBS index!")

    kind = KindDirectory()

