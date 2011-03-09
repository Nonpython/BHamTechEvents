$(document).ready(function() {
    $( "#tags-autocomplete" ).autocomplete({
        source: "http://www.bhamtechevents.org/autocomplete",
        minLength: 2
    });
});