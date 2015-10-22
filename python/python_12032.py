# Using AJAX in django to delete a row in a table represented by a model
$.post('/django/url/to/your/view', {idToDelete: 'value'}, function(response) {
  // callback
});
