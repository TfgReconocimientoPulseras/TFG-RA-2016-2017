<?php
	if(isset($_POST['myData']) && isset($_POST['filename'])){
	 	$obj = json_decode($_POST['myData']);

	 	$myfile = fopen($_POST['filename'].".csv", "w") or die("Unable to open file!");

	    foreach($obj as $o)
	    {
	        $text = $o->ts.';'.$o->ga.';'.$o->gb.';'.$o->gg.';'.$o->ax.';'.$o->ay.';'.$o->az.PHP_EOL;
	        fwrite($myfile, $text);
	    }
	
		//fwrite($myfile, $_POST['myData']);
		fclose($myfile);
	}
?>