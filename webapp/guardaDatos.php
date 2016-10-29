<?php
	if(isset($_POST['myData']) && isset($_POST['nombreUsu']) && isset($_POST['tiempoGrabacion']) && isset($_POST['actividad'])){

	 	$obj = json_decode($_POST['myData']);

	 	

	 	$usu = $_POST['nombreUsu'];
	 	$tiempo = $_POST['tiempoGrabacion'];
	 	$actividad = $_POST['actividad'];
		$nombre = $usu . "_" . $actividad . "_" . $tiempo . "_" . date("m-d-Y G;i;s");
	 	

	 	$myfile = fopen("datos/".$nombre.".csv", "w") or die("Unable to open file!");
	 	fwrite($myfile, 'sep=;'.PHP_EOL);
	 	fwrite($myfile, 'timestamp;gyro-alpha;gyro-beta;gyro-gamma;accel-x;accel-y;accel-z'.PHP_EOL);
	    foreach($obj as $o)
	    {
	        $text = $o->ts.';'.$o->ga.';'.$o->gb.';'.$o->gg.';'.$o->ax.';'.$o->ay.';'.$o->az.PHP_EOL;
	        fwrite($myfile, $text);
	    }
	
		//fwrite($myfile, $_POST['myData']);
		fclose($myfile);
	}
?>