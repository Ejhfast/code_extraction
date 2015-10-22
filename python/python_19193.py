# WhatsApp: how to decode the *.db.crypt files?
$crypt = file_get_contents('msgstore.db.crypt');
$key = pack('H*', '346a23652a46392b4d73257c67317e352e3372482177652c');
$decrypt = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $key, $crypt, MCRYPT_MODE_ECB);
