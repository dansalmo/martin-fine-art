#Simple SPA (Single Page App)

* Single Page App - Page loads once, all other content is Ajax based
* Navigation history works with browser back button
* Content pages are trackable by Google Analytics
* Responsive, viewable on Phone or Desktop 
* Based on Google App Engine, Bootstrap and history.js
* Just create a page body and add a link to it.
* See main.py and static/js/sspa.js for the code
* [Example site](http://martin-fine-art.appspot.com/)

To run local server:

    $ dev_appserver.py .

To deploy:

    $ appcfg.py update .
