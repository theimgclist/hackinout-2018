$(document).ready(function() {

	console.log( "ready!" );

	$("#lalalala").click(function(event){
		alert("senddatabutton clicked");
		$.ajax({
			url: '/newuserdata',
            enctype: 'multipart/form-data',
            data: {a: 'a', b: 'b'},
            type: "POST", //ADDED THIS LINE
            // ... Other options like success and etc
            success: function(msg){
                //alert(msg);
                document.getElementById("my_camera_div").style.display = "block";
                document.getElementById("my_result_div").style.display = "none";
                alert(msg);
            },
            error: function(msg){
                alert("failure : "+msg);
                document.getElementById("my_camera_div").style.display = "block";
                document.getElementById("my_result_div").style.display = "none";
            }
		});
	});


	$('#opt1').click(function(){
		document.getElementById("oldusersenddatabutton").style.display = "block";
		document.getElementById("newuserenterdetailsform").style.display = "none";
		document.getElementById("newusercaptureresetbuttonset").style.display = "none";
	});

	$('#opt2').click(function(){
		document.getElementById("oldusersenddatabutton").style.display = "none";
		document.getElementById("newuserenterdetailsform").style.display = "block";
		document.getElementById("newusercaptureresetbuttonset").style.display = "flex";
	});

});