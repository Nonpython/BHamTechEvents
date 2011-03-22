/*
     Initialize and render the MenuBar when its elements are ready
     to be scripted.
*/

YAHOO.util.Event.onContentReady("topnavbar", function () {

    /*
         Instantiate a MenuBar:  The first argument passed to the
         constructor is the id of the element in the page
         representing the MenuBar; the second is an object literal
         of configuration properties.
    */

    var oMenuBar = new YAHOO.widget.MenuBar("topnavbar", {
                                                autosubmenudisplay: true,
                                                hidedelay: 750,
                                                lazyload: true });

    /*
         Call the "render" method with no arguments since the
         markup for this MenuBar instance is already exists in
         the page.
    */

    oMenuBar.render();

    $(".yui-menu-shadow").remove();

});