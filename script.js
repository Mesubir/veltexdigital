// SAFE PRO Clean URL (No blank screen, no redirect loop)
(function () {

  // Remove .html from URL safely
  function cleanURL() {

    var path = window.location.pathname;

    if (path.endsWith(".html")) {

      var clean = path.substring(0, path.length - 5);

      window.history.replaceState(null, null, clean);

    }

  }

  // Run only once when page fully loads
  window.addEventListener("DOMContentLoaded", function () {

    cleanURL();

  });

})();
