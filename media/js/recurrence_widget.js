 $(document).ready(function(){
	$('#freq_0').click(function() {
	    $('#daily').show("slow");
	    $('#weekly').hide();
	    $('#monthly').hide();
	    $('#annually').hide();
	});
	$('#freq_1').click(function() {
	    $('#daily').hide();
	    $('#weekly').show("slow");
	    $('#monthly').hide();
	    $('#annually').hide();
	});
	$('#freq_2').click(function() {
	    $('#daily').hide();
	    $('#weekly').hide();
	    $('#monthly').show("slow");
	    $('#annually').hide();
	});
	$('#freq_3').click(function() {
	    $('#daily').hide();
	    $('#weekly').hide();
	    $('#monthly').hide();
	    $('#annually').show("slow");
	});
});