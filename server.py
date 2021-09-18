from http.server import BaseHTTPRequestHandler, HTTPServer
import os

x = [ ]
lst = os.listdir()

def b():
	"<ul>"
	for i in range(11):
		# "<ul>"
		a = "<li>" + str(i) + "/<li>"
	"</ul>"
	# return a

class handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()


# def generate_actual_stuff(n):
# 	start ="<img src=\"https://d308ljkq6e62o1.cloudfront.net/img/ni0nIiXtRHy77GQF5i5ZlA/mobile/file\">" +\
# 				"<ol>" 
# 	for i in range(n):
# 		start += "<li><marquee><b>"+ str(i) + "</b> <u>"+ str(random.random())+ "</u></marquee></li>"
# 	start +=				"</ol>"
# 	return start


		# if self.path[1:] == '':
		basic_output_start = "<html>" + \
		"<head>"+ \
			"<title>My Title</title>" +\
		"</head>"+ \
		"<body>" + \
		"<ul>" 
		for i in range(3):
			basic_output_start += "<li>" + "TEST" + "</li>"
		# "<li>" + "TEST" + "</li>" +\
		# "<li>" + "TEST" + "</li>"+\



		basic_output_start += "</ul>" + \
		"</body>" + \
		"</html>"

		# b()
		# "<ol>"

		# for i in lst:
		# 	a = "<li>"+str(i)+"</li>"
		# "</ol>"
			# self.wfile.write(bytes(i, 'utf8'))
		# "</body>" + \
		# "</html>"


			# actual_stuff = generate_actual_stuff(int(self.path[1:]))
			# basic_output_end =			"</body>"+ \
			# "</html>"
			# output = basic_output_start + actual_stuff + basic_output_end
		self.wfile.write(bytes(basic_output_start,'utf-8'))

			# for i in lst:
			# 	self.wfile.write(bytes(i, 'utf8'))
		
		# if self.path[1:] != '':

		# 	if os.path.isdir(self.path[1:]):
		# 		os.chdir(self.path[1:])
		# 		lst1 = os.listdir()
		# 		for j in lst1:
		# 			self.wfile.write(bytes(j, 'utf8'))
		# 		x.append(self.path)

		# 	elif os.path.isfile(self.path[1:]):
		# 		with open(self.path[1:], 'rb')as f:
		# 			self.wfile.write(f.read())

		# 	elif x[0] in self.path:
		# 		y = self.path.replace(x[0], '').replace('/','')
		# 		print(x)
		# 		print(y)
		# 		if os.path.isfile(y):
		# 			with open(y, 'rb')as f:
		# 				self.wfile.write(f.read())

try:
	with HTTPServer(('localhost', 1233), handler) as server:
		server.serve_forever()
except KeyboardInterrupt:
	pass


# import os
# from http.server import HTTPServer, CGIHTTPRequestHandler

# os.chdir('.')
# server_object = HTTPServer(server_address=('', 1234), RequestHandlerClass=CGIHTTPRequestHandler)
# server_object.serve_forever()


# jk = 'txt_files/data.txt'
# l = ['txt_files']


# if l[0] in jk:
# 	print('yes')
# 	i = jk.replace('txt_files','')
# 	print(i)