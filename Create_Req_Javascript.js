function createRequest() {
  var result = null;
  if (window.XMLHttpRequest) {
    // FireFox, Safari, etc.
    result = new XMLHttpRequest();
    if (typeof xmlhttp.overrideMimeType != 'undefined') {
      result.overrideMimeType('text/xml'); // Or anything else
    }
  }
  else if (window.ActiveXObject) {
    // MSIE
    result = new ActiveXObject("Microsoft.XMLHTTP");
  } 
  else {
    // No known mechanism -- consider aborting the application
  }
  return result;
}