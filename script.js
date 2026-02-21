// FULL PRO Clean URL System
(function () {

  // Remove .html from URL
  function cleanURL() {

    var path = window.location.pathname;

    if (path.endsWith(".html")) {

      var clean = path.slice(0, -5);

      window.history.replaceState({}, document.title, clean);

    }

  }

  // Handle clicks automatically
  function handleLinks() {

    document.addEventListener("click", function(e) {

      var target = e.target;

      if (target.tagName === "A") {

        var href = target.getAttribute("href");

        if (href && href.endsWith(".html")) {

          e.preventDefault();

          var clean = href.replace(".html", "");

          window.history.pushState({}, "", clean);

          window.location.href = href;

        }

      }

    });

  }

  // Handle back/forward buttons
  window.addEventListener("popstate", function() {

    var path = window.location.pathname;

    if (!path.endsWith(".html")) {

      window.location.href = path + ".html";

    }

  });

  // Run functions
  window.addEventListener("load", function() {

    cleanURL();

    handleLinks();

  });

})();
