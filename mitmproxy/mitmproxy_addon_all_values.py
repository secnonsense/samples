import datetime

def response(flow):
    file="response_proxy_test.txt"
    with open(file, 'a') as output:
        #output.write(f"Flow request values: {dir(flow.response)}\n")
        output.write(f"\n=================================================================================\n")
        output.write(f"Flow response value _abc_impl: {flow.response._abc_impl}\n")
        output.write(f"Flow response values _get_content_type_charset: {flow.response._get_content_type_charset}\n")
        output.write(f"Flow response values _get_cookies: {flow.response._get_cookies}\n")
        output.write(f"Flow response values _guess_encoding: {flow.response._guess_encoding}\n")
        output.write(f"Flow response values _set_cookies: {flow.response._set_cookies}\n")
        output.write(f"Flow response values content: {flow.response.content}\n")
        output.write(f"Flow response values cookies: {flow.response.cookies}\n")
        output.write(f"Flow response values copy: {flow.response.copy}\n")
        output.write(f"Flow response values data: {flow.response.data}\n")
        output.write(f"Flow response values decode: {flow.response.decode}\n")
        output.write(f"Flow response values encode: {flow.response.encode}\n")
        output.write(f"Flow response values from_state: {flow.response.from_state}\n")
        output.write(f"Flow response values get_content: {flow.response.get_content}\n")
        output.write(f"Flow response values get_state: {flow.response.get_state}\n")
        output.write(f"Flow response values get_text: {flow.response.get_text}\n")
        output.write(f"Flow response values headers: {flow.response.headers}\n")
        output.write(f"Flow response values http_version: {flow.response.http_version}\n")
        output.write(f"Flow response values json: {flow.response.json}\n")
        output.write(f"Flow response values make: {flow.response.make}\n")
        output.write(f"Flow response values raw_content: {flow.response.raw_content}\n")
        output.write(f"Flow response values reason: {flow.response.reason}\n")
        output.write(f"Flow response values refresh: {flow.response.refresh}\n")
        output.write(f"Flow response values set_content: {flow.response.set_content}\n")
        output.write(f"Flow response values set_state: {flow.response.set_state}\n")
        output.write(f"Flow response values set_text: {flow.response.set_text}\n")
        output.write(f"Flow response values status_code: {flow.response.status_code}\n")
        output.write(f"Flow response values stream: {flow.response.stream}\n")
        output.write(f"Flow response values text: {flow.response.text}\n")
        output.write(f"Flow response values timestamp_start: {datetime.datetime.fromtimestamp(flow.response.timestamp_start)}\n")
        output.write(f"Flow response values timestamp_end: {datetime.datetime.fromtimestamp(flow.response.timestamp_end)}\n")
        output.write(f"Flow response values trailers: {flow.response.trailers}\n")
        
       # '_abc_impl', '_get_content_type_charset', '_get_cookies', '_guess_encoding', '_set_cookies', 'content', 'cookies', 'copy', 'data', 'decode', 'encode', 'from_state', 'get_content', 'get_state', 'get_text', 'headers', 'http_version', 'is_http10', 'is_http11', 'is_http2', 'json', 'make', 'raw_content', 'reason', 'refresh', 'set_content', 'set_state', 'set_text', 'status_code', 'stream', 'text', 'timestamp_end', 'timestamp_start', 'trailers'

def request(flow):
    file="request_proxy_test.txt"
    with open(file, 'a') as output:
        #output.write(f"Flow request values: {dir(flow.request)}\n")
        output.write(f"\n=================================================================================\n")
        output.write(f"Flow request value _abc_impl: {flow.request._abc_impl}\n")
        output.write(f"Flow request values _get_content_type_charset: {flow.request._get_content_type_charset}\n")
        output.write(f"Flow request values _get_cookies: {flow.request._get_cookies}\n")
        output.write(f"Flow request values _get_multipart_form: {flow.request._get_multipart_form}\n")
        output.write(f"Flow request values _get_query: {flow.request._get_query}\n")
        output.write(f"Flow request values _get_urlencoded_form: {flow.request._get_urlencoded_form}\n")
        output.write(f"Flow request values _guess_encoding: {flow.request._guess_encoding}\n")
        output.write(f"Flow request values _set_cookies: {flow.request._set_cookies}\n")
        output.write(f"Flow request values _set_multipart_form: {flow.request._set_multipart_form}\n")
        output.write(f"Flow request values _set_query: {flow.request._set_query}\n")
        output.write(f"Flow request values _set_urlencoded_form: {flow.request._set_urlencoded_form}\n")
        output.write(f"Flow request values anticache: {flow.request.anticache}\n")
        output.write(f"Flow request values anticomp: {flow.request.anticomp}\n")
        output.write(f"Flow request values authority: {flow.request.authority}\n")
        output.write(f"Flow request values constrain_encoding: {flow.request.constrain_encoding}\n")
        output.write(f"Flow request values content: {flow.request.content}\n")
        output.write(f"Flow request values cookies: {flow.request.cookies}\n")
        output.write(f"Flow request values copy: {flow.request.copy}\n")
        output.write(f"Flow request values data: {flow.request.data}\n")
        output.write(f"Flow request values decode: {flow.request.decode}\n")
        output.write(f"Flow request values encode: {flow.request.encode}\n")
        output.write(f"Flow request values first_line_format: {flow.request.first_line_format}\n")
        output.write(f"Flow request values from_state: {flow.request.from_state}\n")
        output.write(f"Flow request values get_content: {flow.request.get_content}\n")
        output.write(f"Flow request values get_state: {flow.request.get_state}\n")
        output.write(f"Flow request values get_text: {flow.request.get_text}\n")
        output.write(f"Flow request values headers: {flow.request.headers}\n")
        output.write(f"Flow request values host: {flow.request.host}\n")
        output.write(f"Flow request values host_header: {flow.request.host_header}\n")
        output.write(f"Flow request values http_version: {flow.request.http_version}\n")
        output.write(f"Flow request values json: {flow.request.json}\n")
        output.write(f"Flow request values make: {flow.request.make}\n")
        output.write(f"Flow request values method: {flow.request.method}\n")
        output.write(f"Flow request values multipart_form: {flow.request.multipart_form}\n")
        output.write(f"Flow request values path: {flow.request.path}\n")
        output.write(f"Flow request values path_components: {flow.request.path_components}\n")
        output.write(f"Flow request values port: {flow.request.port}\n")
        output.write(f"Flow request values pretty_host: {flow.request.pretty_host}\n")
        output.write(f"Flow request values pretty_url: {flow.request.pretty_url}\n")
        output.write(f"Flow request values query: {flow.request.query}\n")
        output.write(f"Flow request values raw_content: {flow.request.raw_content}\n")
        output.write(f"Flow request values scheme: {flow.request.scheme}\n")
        output.write(f"Flow request values set_content: {flow.request.set_content}\n")
        output.write(f"Flow request values set_state: {flow.request.set_state}\n")
        output.write(f"Flow request values set_text: {flow.request.set_text}\n")
        output.write(f"Flow request values stream: {flow.request.stream}\n")
        output.write(f"Flow request values text: {flow.request.text}\n")
        output.write(f"Flow request values timestamp_start: {datetime.datetime.fromtimestamp(flow.request.timestamp_start)}\n")
        output.write(f"Flow request values timestamp_end: {datetime.datetime.fromtimestamp(flow.request.timestamp_end)}\n")
        output.write(f"Flow request values trailers: {flow.request.trailers}\n")
        output.write(f"Flow request values url: {flow.request.url}\n")
        output.write(f"Flow request values urlencoded_form: {flow.request.urlencoded_form}\n")
        
        
        
        
        # '_abc_impl', '_get_content_type_charset', '_get_cookies', '_get_multipart_form', '_get_query', '_get_urlencoded_form', '_guess_encoding', '_set_cookies', '_set_multipart_form', '_set_query', '_set_urlencoded_form', 'anticache', 'anticomp', 'authority', 'constrain_encoding', 'content', 'cookies', 'copy', 'data', 'decode', 'encode', 'first_line_format', 'from_state', 'get_content', 'get_state', 'get_text', 'headers', 'host', 'host_header', 'http_version', 'is_http10', 'is_http11', 'is_http2', 'json', 'make', 'method', 'multipart_form', 'path', 'path_components', 'port', 'pretty_host', 'pretty_url', 'query', 'raw_content', 'scheme', 'set_content', 'set_state', 'set_text', 'stream', 'text', 'timestamp_end', 'timestamp_start', 'trailers', 'url', 'urlencoded_form']
