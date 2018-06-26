function resetRegisterModal(form, formfields, blanksMessage, emailMessage, passwordMessage) {
    blanksMessage.style.display = "none";
    emailMessage.style.display = "none";
    passwordMessage.style.display = "none";
    form.reset();
    //return style colour to original colour (if it has been altered by invalid styles)
    for(var i = 0; i < formfields.length; i++) {
        var reqField = formfields[i];
        var reqFieldIDName = reqField.attr('id');
        $("label[for='"+reqFieldIDName+"']").css("color", "#5A634D");
        reqField.css("border-bottom", "1px solid #5A634D");
    }
}


function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function fieldInvalidStyling(field){
    var reqFieldIDName = field.attr('id');
    // changes label, text and border bottom color to pink
    $("label[for='"+reqFieldIDName+"']").css("color", "#FE7460");
    field.css("color", "#FE7460");
    field.css("border-bottom", "1px solid #FE7460");

    // changes everything back to green when user clicks into field
    field.focus(function () {
        var name = $(this).attr('id');
        $("label[for='"+name+"']").css("color", "#5A634D");
        $(this).css("color", "#5A634D");
        $(this).css("border-bottom", "1px solid #5A634D");
    });
}






function fieldValidStyling(field) {
    var reqFieldIDName = field.attr('id');
    $("label[for='"+reqFieldIDName+"']").css("color", "#5A634D");
    field.css("border-bottom", "1px solid #5A634D");
}

function passwordInvalidStyling(field) {
    // changes label, field text and border bottom color to pink
    $("label[for='"+field.attr('id')+"']").css("color", "#FE7460");
    field.css("color", "#FE7460");
    field.css("border-bottom", "1px solid #FE7460");

    // changes everything back to green when user clicks into field
    // and erases invalid password
    field.focus(function () {
        $(this).val('');
        var name = $(this).attr('id');
        $("label[for='"+name+"']").css("color", "#5A634D");
        $(this).css("color", "#5A634D");
        $(this).css("border-bottom", "1px solid #5A634D");
    });

}


function displayElement(element){
    element.style.display = "block";
}

function hideElement (element){
    element.style.display = "none";
}



