from quixote import enable_ptl
from quixote.publish import Publisher

enable_ptl()
from site import RootDirectory

# For database setting
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def create_publisher():
    return Publisher(RootDirectory(), display_exceptions='plain')
