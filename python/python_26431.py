# Jupyter (iPython Notebook) interface strange white bar at bottom of screen
$([IPython.events]).on("app_initialized.NotebookApp", function () {
$('div#header').hide();});
