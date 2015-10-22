# In SugarCRM API, how do I get a user's timezone info?
&lt;?php
    // $user being a User Object
    $timezone = TimeDate::userTimezone($user);
