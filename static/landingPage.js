//checks script connection success
console.log("connected");

//Set h1 animation to repeat every 2seconds
$(document).ready(function() {
	setInterval(function() {
		$("#main").toggleClass("is-loading");
	}, 2500)
});

//change h1 text when submit btn clicked
//send info to bot script
$("#submitBtn").click(function(){
	//display confirmation text for 10secs

	$("h1").text("Reminder Set!");
	setTimeout(function(){
		$("h1").text("Set Reminder");
	}, 10000);


	var url = "/makeapointment"; // the script where you handle the form input.

	$.ajax({
           type: "POST",
           url: url,
           data: $("#idForm").serialize(), // serializes the form's elements.
           success: function(data)
           {
               console.log(data); // show response from the php script.
           }
         });

    return false; // avoid to execute the actual submit of the form.
});
