<?php

echo "Password: ";
system('stty -echo');
$password = trim(fgets(STDIN));
system('stty echo');
