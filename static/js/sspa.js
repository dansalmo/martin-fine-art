

$(document).ready(function () {

  var ajaxContentReady = function () {
      // Fits videos in fluid grid
    $(".hero-unit").fitVids({ customSelector: "object[src^='/']"});
    console.log('contentReady');
  };

  // colapse touch menu when link is clicked
  var navMain = $(".navbar-collapse");

  navMain.on("click", "a", null, function () {
     navMain.collapse('hide');
  });

  ajaxContentReady();

  var updateNav = function(urlPath) {
  $('a[href="' + urlPath + '"]').parent().addClass('active').siblings('.active').removeClass('active');
  };

  // History.js - HTML5 History API handling 
  var History = window.History;
  if (History.enabled) {
      State = History.getState();
      // set initial state to first page that was loaded
      console.log(window.location.pathname);
      History.pushState({urlPath: window.location.pathname}, $("title").text(), State.urlPath);
      updateNav(window.location.pathname);
  } else {
      return false;
  }

  var loadAjaxContent = function(target, urlBase, selector) {
  // retrieves #selector from server and places appends it to #target
  // sets class="hidden" for all siblings in target 
      $('#ajax_content').load(urlBase + ' ' + selector, function(response, status, xhr) {
          if (status == "error") {
            var msg = '<div id="' + selector.substring(1) + '">You must <a href="' + $('#not-signed-in').attr('href') + '">Sign in or register</a> to use this feature</div>';
            $('#ajax_content').html(msg);
          }
          $(selector).appendTo(target).siblings().addClass('hidden');
          ajaxContentReady();
          console.log('lAC', target,' ', urlBase, 'sel=', selector);
      });
  };

  function addslashes( str ) {
      return (str+'').replace(/([\\"'])/g, "\\$1").replace(/\0/g, "\\0");
  }
  var updateContent = function(State) {
      // uses the path with cleaned up query string as the selector
      var selector = ('#' + State.data.urlPath.substring(1).replace(/[?=&%]/g,"-"));
  //    var selector = ('#' + State.data.urlPath.substring(1)).split('?')[0];
      console.log('url=', State.url,' selector=', selector);
      if ($(selector).length) { //content is already loaded but hidden
          $(selector).siblings().addClass('hidden');
          $(selector).removeClass('hidden');
      } else {
          loadAjaxContent('#content', State.url, selector);
      }
  };

  // Content update and back/forward button handler
  History.Adapter.bind(window, 'statechange', function() {
  console.log('HAb');
      updateNav(window.location.pathname);
  console.log('after editAF ', History.getState());
      updateContent(History.getState());
  });

  // navigation link handler
  $('body').on('click', 'a:not(.no-ajax, .btn-navbar, .dropdown-toggle)', function(e) {
   console.log('Navlink');
      var urlPath = $(this).attr('href');
      var title = $(this).text();
      $('.dropdown.open .dropdown-toggle').dropdown('toggle');
      $('html, body').animate({ scrollTop: 0 }, 'slow');
      History.pushState({urlPath: urlPath}, title, urlPath);
      return false; // prevents default click action of <a ...>
  });
});
