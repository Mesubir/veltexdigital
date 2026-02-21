// Universal .html URL remover
(function() {

  function removeHtmlFromURL() {

    var path = window.location.pathname;

    if (path.endsWith(".html")) {

      var cleanURL = path.slice(0, -5);

      window.history.replaceState(null, null, cleanURL);

    }

  }

  // Run when page loads
  window.addEventListener("load", removeHtmlFromURL);

})();
