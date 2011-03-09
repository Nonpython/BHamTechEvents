$(document).ready(function() {
    var tallest = max(
        $("#lsidebar").height(),
        $("#maincontent").height(),
        $("#rsidebar").height()
    );
    $("#lsidebar,#maincontent,#rsidebar").height(tallest);
    
});