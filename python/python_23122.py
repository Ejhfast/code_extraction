# Python: how to send html-code in a POST request
$desc = JRequest::getVar('description', '', 'POST', 'string', JREQUEST_ALLOWHTML);
