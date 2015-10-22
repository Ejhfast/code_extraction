# How do I detect when a user has been idle for a certain time and destroy their session in PHP?
$SESSION['lastActivity'] &lt; time() - &lt;your idle time&gt;
