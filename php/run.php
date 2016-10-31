<?php
$content = file_get_contents(__DIR__.'/darwin_utf8.txt');
$arr = explode('。', $content);
array_pop($arr);
foreach ($arr as $key => $value) echo $value."。\n";
