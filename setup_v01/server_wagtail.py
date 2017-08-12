# CherryPy-Server for WSGI-Application (Wagtail)
# Based on a [Tutorial by DigitalOcean]() 
# modified by felix@42sol.eu
# copy this to {{full-path-to-base-app-folder}}
# use mustache to make this script usable
from {{app-name}}.wsgi import application

import cherrypy # url: http://docs.cherrypy.org/en/latest/
 
def main( x_s_app_path = '/' ):
    # -[1] Mount the application
    cherrypy.tree.graft(application, x_s_app_path)

    # -[2] unsubscribe default server
    cherrypy.server.unsubscribe()

    # -[3] create the new server object
    l_o_server = cherrypy._cpserver.Server()
    
    # -[4] setup apps
    setup_app(l_o_server, {{app-name-1}}, {{app-port-1}}) # use default parameters for host ip-address (local host)
    
    l_o_server2 = cherrypy._cpserver.Server()
    setup_app(l_o_server2, {{app-name-2}}, {{app-port-2}}) # use default parameters for host ip-address (local host)
     
    # -[5] start-up server engines
    cherrypy.engine.start()
    cherrypy.engine.block()

def setup_app( x_o_server, x_s_app_name, x_u_host_port, x_s_host_ip = '127.0.0.1', x_u_thread_pool = 30 ):
    # Configure the server object
    x_o_server.socket_host = x_s_host_ip
    x_o_server.socket_port = x_u_host_port
    x_o_server.thread_pool = x_u_thread_pool

    # @note: For SSL Support
    # x_o_server.ssl_module            = 'pyopenssl'
    # x_o_server.ssl_certificate       = 'ssl/certificate.crt'
    # x_o_server.ssl_private_key       = 'ssl/private.key'
    # x_o_server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    x_o_server.subscribe()


if __name__ == '__main__':
  main()
