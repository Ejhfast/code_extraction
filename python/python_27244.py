# How to make a server side data request via react.js
$.get('/get_dataset.json', function(dataset) {
  React.renderComponent( &lt;App data={dataset}/&gt;, document.getElementById( "App" ) );
});
