# Converting two python lines code to PHP
&lt;?php
    $vowels ='/[\x{064B}-\x{0652}]/u';
    $newstr = preg_replace($vowels,"",$str);
