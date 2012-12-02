#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib
import os
import jinja2

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'templates')), autoescape = True)


class MainHandler(webapp2.RequestHandler):
	def write(self,*a,**kw):
		self.response.out.write(*a,**kw)

	def render_str(self,template,**params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self,template,**kw):
		self.write(self.render_str(template,**kw))

	def read_secure_cookie(self, name):
		cookie_val = self.request.cookies.get(name)
		return cookie_val and check_secure_val(cookie_val)

	def get(self):
		self.response.out.write('Hello world!')

class Home_page(MainHandler):
	def get(self):
		self.render('home.html')

class People_page(MainHandler):
	def get(self):
		self.render('people.html')

class Performance_page(MainHandler):
	def get(self):
		self.render('performance.html')

class Contact_page(MainHandler):
	def get(self):
		self.render('contact.html')
	def post(self):
		self.message = self.request.get('send')
		self.render('contact.html', message = "Thanks! Wel'll get back to you within the next week.")

app = webapp2.WSGIApplication([('/', Home_page),
							   ('/home', Home_page ),
                               ('/people', People_page),
                               ('/performance', Performance_page),
                               ('/contact', Contact_page)],debug=True) 
