 $(document).ready(function(){

    // Hide and toggle search bar on mobile devives
    $(".search-bar1").hide();
    $(".search-icon").click(function(){
        $(".search-bar1").toggle();
    });

    // Multi-Level Dropdowns from w3schools
    
    $('.dropdown a.level').on("click", function(e){
        $(this).next('ul').toggle();
        e.stopPropagation();
        e.preventDefault();
    });

    $("a.level").click(function(){
        $(this).toggleClass("bold");
        $('a.level ul').hide();
    });
});
