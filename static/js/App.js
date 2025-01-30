$(document).ready(function () {
    $("#id_btn_menu").click(function (e) { 

        if($("#id_navbar").is(":visible")) {
            $("#id_navbar").hide()
            $("#id_btn_menu").removeClass("active");
        } 
        else {
            $("#id_navbar").css('display', 'flex')
            $("#id_btn_menu").addClass("active");
        }
    });

});