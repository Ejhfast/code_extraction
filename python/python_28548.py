# Google Analytics User-ID returning Uncaught ReferenceError: None is not defined when user is not logged | Python
if('{{request.user.id}}'!='None') {
  ga('set', '&amp;uid', {{request.user.id}});
  }
