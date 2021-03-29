def app(environ, start_response):
    """
    A WSGI app; starting point for web framework.
    """
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [b'Hi; Response from a simple WSGI application.\n']
