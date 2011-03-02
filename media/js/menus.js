$(document).ready(function(){ 
    var sel = 'a[href="' + $(location).attr('href') + '"]'
	$(sel).addClass("button-active")
	$(".button")..mouseover(function() {
	  $(this).addClass("button-active");
	});
	
	$(".button")..mouseleave(function() {
	  $(this).delClass("button-active");
	});

});