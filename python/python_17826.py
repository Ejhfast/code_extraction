# Issuing reading JSON from POST
var_dump(json_decode(file_get_contents("php://input")));
