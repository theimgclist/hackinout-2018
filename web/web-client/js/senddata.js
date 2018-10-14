$(document).ready(function() {

	console.log( "ready!" );

	$('#opt1').click(function(){
		document.getElementById("oldusersenddatabutton").style.display = "block";
		document.getElementById("newuserenterdetailsform").style.display = "none";
	});

	$('#opt2').click(function(){
		document.getElementById("oldusersenddatabutton").style.display = "none";
		document.getElementById("newuserenterdetailsform").style.display = "block";
	});

});