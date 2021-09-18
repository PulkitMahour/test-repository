from http.server import BaseHTTPRequestHandler, HTTPServer
import os

x = [ ]
lst = os.listdir()

def create_list():
	"<ul>"
	a = ""
	for i in range(11):
		a += "<li>" + str(i) + "/<li>"
	"</ul>"
	return a 
	# return a

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		basic_output_start = "<html>" + \
		"<head>"+ \
			"<title>My Title</title>" +\
		"</head>"+ \
		"<body>" + \
		"<ul>" 
		for i in range(3):
			basic_output_start += "<li>" + "TEST" + "</li>"



		basic_output_start += "</ul>" + \
		"</body>" + \
		"</html>"

		self.wfile.write(bytes(basic_output_start,'utf-8'))


try:
	with HTTPServer(('localhost', 1233), handler) as server:
		server.serve_forever()
except KeyboardInterrupt:
	pass


