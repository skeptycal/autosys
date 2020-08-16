<?php

require("../src/toml.php");

$arr = array (
	'a' => 1,
	'b' => array (1, 2, 3),
	'c' => array ('a' => 'apple', 'b' => array(4, 5, 6)),
	'd' => true
	);

$encoder = new Toml_Encoder();
echo $encoder->encode($arr);

?>
