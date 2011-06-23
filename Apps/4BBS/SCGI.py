from flup.server.scgi import WSGIServer
from quixote import enable_ptl
enable_ptl()
from quixote.publish import Publisher
import sys
from Root.site import RootDirectory

import thread
from quixote.wsgi import QWIP

class ThreadedPublisher(Publisher):
    is_thread_safe = True 
    def __init__ (self,root_namespace,logger=None,session_manager=None,config=None): 
        Publisher.__init__(self, root_namespace,logger,session_manager, config) 
        self._request_dict = {} 

    def _set_request(self, request): 
        self._request_dict[thread.get_ident()] = request 

    def _clear_request(self): 
        try: 
            del self._request_dict[thread.get_ident()] 
        except KeyError: 
            pass 

    def get_request(self): 
        return self._request_dict.get(thread.get_ident())


# Session
from quixote.session import Session, SessionManager
class BBS_Session(Session):

    def __init__(self, id):
        Session.__init__(self, id)
        self.num_requests = 0

    def start_request(self):
        """
        This is called from the main object publishing loop whenever
        we start processing a new request.  Obviously, this is a good
        place to track the number of requests made.  (If we were
        interested in the number of *successful* requests made, then
        we could override finish_request(), which is called by
        the publisher at the end of each successful request.)
        """
        Session.start_request(self)
        self.num_requests += 1

    def has_info(self):
        """
        Overriding has_info() is essential but non-obvious.  The
        session manager uses has_info() to know if it should hang on
        to a session object or not: if a session is "dirty", then it
        must be saved.  This prevents saving sessions that don't need
        to be saved, which is especially important as a defensive
        measure against clients that don't handle cookies: without it,
        we might create and store a new session object for every
        request made by such clients.  With has_info(), we create the
        new session object every time, but throw it away unsaved as
        soon as the request is complete.

        (Of course, if you write your session class such that
        has_info() always returns true after a request has been
        processed, you're back to the original problem -- and in fact,
        this class *has* been written that way, because num_requests
        is incremented on every request, which makes has_info() return
        true, which makes SessionManager always store the session
        object.  In a real application, think carefully before putting
        data in a session object that causes has_info() to return
        true.)
        """
        return (self.num_requests > 0) or Session.has_info(self)

    is_dirty = has_info

def main():
    from quixote import logger
    Logger = logger.DefaultLogger(access_log="acess_log.txt",error_log="error_log.txt")
    app = QWIP(ThreadedPublisher(RootDirectory(),logger=Logger,session_manager=SessionManager(session_class=BBS_Session)))
    #app = QWIP( create_publisher())
    ret = WSGIServer(app).run()

if __name__ == "__main__":
    main()
