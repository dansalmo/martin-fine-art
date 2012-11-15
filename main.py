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
import webapp2, os, json
from google.appengine.ext.webapp import template
from google.appengine.api import urlfetch
from lxml import etree, html
from lxml.html import tostring, fragment_fromstring
from google.appengine.api import users

def innerHTML(file, tag):
  tree = html.parse(file)
  return ''.join([tostring(child) for child in tree.xpath(tag)[0].iterchildren()])

class GetPage(webapp2.RequestHandler):
    def get(self):
        if self.request.path == '/':
          return self.redirect('/home')

        page = self.request.path[1:]
        template_values = {
                'content': innerHTML(page + '.html', 'body'),
                'content_id': page,
                }

        path = os.path.join(os.path.dirname(__file__), 'index-template.html' )
        self.response.out.write(template.render(path, template_values))

#incomplete - finish if needed
def LogIn():
    user = users.get_current_user()
    if user:
        greeting = ("<div class=\"signed-in\"> %s <a class=\"sign-out\" href=\"%s\">(sign out)</a></div>" %
                    (user.nickname(), users.create_logout_url("/")))
        template_values = {
                'greeting': greeting,
                'user': user.nickname(),
                }
    else:
        greeting = ("<a class=\"sign-in\" href=\"%s\">Sign in or register</a>" %
                    users.create_login_url("/"))
        template_values = {
                'greeting': greeting,
                }
    return
    
app = webapp2.WSGIApplication([('/', GetPage),
                              ('/home', GetPage),
                              ('/about', GetPage),
                              ('/contact', GetPage),
                              ('/schedule', GetPage),
                              ('/pricing', GetPage),
                              ('/art-classes-children', GetPage),
                              ('/art-classes-teens', GetPage),
                              ('/art-classes-adults', GetPage),
                              ('/gallery', GetPage)],
                               debug=True)

                              