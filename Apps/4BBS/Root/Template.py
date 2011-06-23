#_*_ coding:utf-8 _*_

class Template(object):
    """
        HTML % (Title,Body)
    """
    HTML =  """
            <html>
            <head>
                <meta http-equiv="content-type" content="text/html; charset=utf-8">
            
                <title>%s</title>
                
            </head>
            <body>
                %s
            </body>
            </html>
            """

    Kind_Body = """
                    <!-- Top --!>
                    <div>%s</div>

                    <!-- Form --!>
                    <div>%s</div>

                    <!-- Booter --!>
                    <div>%s</div>
                """
    Kind_Top = """
                <div>
                <span><a href="/kind">Index</a></span>
                <span><a href="/kind/new">New Kind</a></span>
                <span><a href="/kind/login">Login</a></span>
                <span><a href="/kind/logout">Logout</a></span>
                </div>
               """

