function helloWorld(){
	console.log("hello world!");
}
function provjera_korinickog_imena(ime) {
	var _username=document.getElementById("txt_reg_user").value;
	if(ime==_username){
		return True;
	}
	else {
		return False;
	}


}
