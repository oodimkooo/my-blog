$(document).ready(function(){
	var myDate = new Date(), 
		myYear = myDate.getFullYear(), 
		myMonth = myDate.getMonth(),
		toDay = new Date(Date.now());
		
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie !== '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};
		
	function fillWeekDays(month, year){
		var firstDay = new Date(year, month, 1),
			lastDay = new Date(year, month + 1, 0);
			monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
			$(".datedays").empty();
			if (firstDay.getDay() !== 1){
				for (var i = firstDay.getDay() - 2; i >= 0 ; i -= 1){
					var prevMonthLastDay = new Date(year, month, 0);
					$(".datedays").append("<div class='dateday prevmonthday'>" + (prevMonthLastDay.getDate() - i) + "</div>");
				}
			}
			for (var i = firstDay.getDate(); i <= lastDay.getDate(); i += 1){
				if (i ==  toDay.getDate() && month == toDay.getMonth() && year == toDay.getFullYear()){
					$(".datedays").append("<div class='dateday currentmonthday today'>" + i + "</div>");
				} else {
					$(".datedays").append("<div class='dateday currentmonthday'>" + i + "</div>");
				}
			}
			if (lastDay.getDay() != 0){
				for (var i = 1; i <= 7 - lastDay.getDay(); i += 1){
					$(".datedays").append("<div class='dateday nextmonthday'>" + i + "</div>");
				}
			}						
			$(".current-month").html(monthNames[month]);
			$(".current-year").html(year);
			$(".dateday").fadeIn();
	}
	
	function getMonthEvents(month, year){
		var data = {"month": month, "year": year};
		$.ajax({
			headers: { "X-CSRFToken": getCookie("csrftoken") },
			type: "GET",
			url: "/booking/get_events/",
			data: data,
			dataType: "json",
			success: function(response){
				events = JSON.parse(response);
				for (var i in events) {
					var eventDay = new Date(Date.parse(events[i].fields.startDate)),
						eventTimeFrom = eventDay.getHours() + ":" + (("0" + eventDay.getMinutes()).slice(-2)),
						eventCreated = Date(Date.parse(events[i].fields.date_created));
					$(".currentmonthday").eq(eventDay.getDate() - 1).addClass("eventday");
					$(".currentmonthday").eq(eventDay.getDate() - 1).append(
					"<div class='description'><h1 class='event-title'>" + events[i].fields.title + "</h1><p class='event-description'>" + events[i].fields.description + "</p><p class='event-time'>" + eventTimeFrom + "</p><p class='event-author'>" + events[i].fields.author + "</p><p class='event-created'>" + eventCreated + "</p></div>"
					);
				}
			}						
		});	
	}
	
	fillWeekDays(myMonth,myYear);
	getMonthEvents(myMonth,myYear)
	
	$(".left").click(function(){
		myYear = myMonth == 0 ? myYear - 1: myYear;
		myMonth = (myMonth - 1)%12 < 0 ? 11 : (myMonth - 1)%12;
		fillWeekDays(myMonth,myYear);
		getMonthEvents(myMonth,myYear);
	});
	
	$(".right").click(function(){
		myMonth = (myMonth + 1)%12;
		myYear = myMonth == 0 ? myYear + 1: myYear;
		fillWeekDays(myMonth,myYear);
		getMonthEvents(myMonth,myYear);
	});
	
	//Получить форму создания события
	$(".datedays").on("click", ".currentmonthday", function (event) {
		$.ajax({
			url: '/booking/set_event/',
			type: 'get',
			dataType: 'json',
			beforeSend: function () {
				$("#myModal").fadeIn();
				$(".modal").css("display","flex");
			},
			success: function (data) {
				console.log(data);
				$(".modal").html(data.html_form);
				$("#input-event-startdate").val(myYear + "-" + (myMonth + 1) + "-" + $(event.target).html());
			}
		});
	});
	
	//Обработка формы создания события
	$("#myModal").on("submit", "#eventCreation", function () {
		var form = $(this);
		$.ajax({
			url: form.attr("action"),
			data: form.serialize(),
			type: form.attr("method"),
			dataType: 'json',
			success: function (data) {
				//console.log("get response");
				//console.log(data);
				if (data.form_is_valid) {
					$("#myModal").fadeOut();
					getMonthEvents(myMonth,myYear);
				}
				else {
					$(".modal").html(data.html_form);
					//console.log(data.html_form);
				}
			}
		});
		return false;	
	});
	
	var modal = document.getElementById('myModal');
	window.onclick = function(event) {
		if (event.target == modal) {
			$("#myModal").fadeOut();
		}
	}
	
});