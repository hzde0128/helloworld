#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2017 All rights reserved.
#
#   Author        : jerry
#   Email         : hzde0128@gmail.com
#   File Name     : t2.py
#   Last Modified : 2017-03-16 15:10
#   Describe      :
#
#   Log           :
#
# ====================================================

import sys
# import os

import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port",default=8000, help="run n the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
	def get(self, input):
		self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
	def post(self):
		text = self.get_argument('text')
		width = self.get_argument('width', 40)
		self.write(textwrap.fill(text, int(width)))

if __name__  == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
			handlers=[
				(r"/reverse/(\w+)",ReverseHandler),
				(r"/wrap", WrapHandler)
				]
			)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
