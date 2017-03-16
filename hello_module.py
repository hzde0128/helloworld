#!/usr/bin/env python
# encoding: utf-8
# coding style: pep8
# ====================================================
#   Copyright (C)2017 All rights reserved.
#
#   Author        : jerry
#   Email         : hzde0128@gmail.com
#   File Name     : hello_module.py
#   Last Modified : 2017-03-16 17:04
#   Describe      :
#
#   Log           :
#
# ====================================================

import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
import os.path

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class HelloHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('hello.html')

class HelloModule(tornado.web.UIModule):
	def render(self):
		return '<h1>Hello, world!</h1>'

if __name__ == "__name__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(
			handlers=[(r'r', HelloHandler)],
			template_path=os.path.join(os.path.dirname(__file__),'templates'),
			ui_modules={'Hello': HelloModule}
			)
	server = tornado.httpserver.HTTPServer(app)
	server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
