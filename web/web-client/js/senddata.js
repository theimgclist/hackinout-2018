$(document).ready(function() {
	// $("#senddatabutton").click(function(event){
	// 	var formData = new FormData();

	// 	formData.append('section', 'general');
	// 	formData.append('action', 'previewImg');
	// 	// Attach file
	// 	formData.append('image', $('input[type=file]')[0].files[0]); 

	// 	$.ajax({
	// 		url: 'localhost:8080/newusersignup',
	// 	    data: formData,
	// 	    type: "POST", //ADDED THIS LINE
	// 	    // THIS MUST BE DONE FOR FILE UPLOADING
	// 	    contentType: false,
	// 	    processData: false,
	// 	    // ... Other options like success and etc
	// 		success: function(msg){
	// 			alert(msg);
	// 		},
	// 		error: function(){
	// 			alert("failure");
	// 		}
	// 	});
	// });

	console.log( "ready!" );


	$("#lalala").click(function(event){
		$.ajax({
			url: 'http://localhost:8080/olduserverify',
			dataType: 'text',
			type: 'POST',
			contentType: 'application/x-www-form-urlencoded',
			data: {a : 'a' , b : 'b'},
			success: function( data, textStatus, jQxhr ){
				alert(data);
			},
			error: function( jqXhr, textStatus, errorThrown ){
				console.log( errorThrown );
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