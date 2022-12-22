$('.open__popup__virtualtour').click(function (e) {
    $('body,html').animate({ scrollTop: 0 }, 400);
    e.preventDefault();
    $('.popup__bg__virtualtour').fadeIn(600);
    $('html').addClass('no-scroll');
});
$('.open__popup__question').click(function (e) {
    $('body,html').animate({ scrollTop: 0 }, 400);
    e.preventDefault();
    $('.popup__bg__question').fadeIn(600);
    $('html').addClass('no-scroll');
});
$('.close__popup__virtualtour').click(function () {
    $('.popup__bg__virtualtour').fadeOut(); (600);
    $('html').removeClass('no-scroll');
});
$('.close__popup__question').click(function () {
    $('.popup__bg__question').fadeOut(); (600);
    $('html').removeClass('no-scroll');
});

$(".form__input").click(function () {
    if (($(this).prop("checked"))) {
        $("#form__button").removeAttr("disabled");
    } else {
        $("#form__button").attr("disabled", "disabled");
    }
})

$('.menu_clk').click(function (e) {
    $('body,html').animate({ scrollTop: 0 }, 400);
    e.preventDefault();
    $('.popup__bg__menu').fadeIn(600);
    $('html').addClass('no-scroll');
});
$('.close__popup__menu_clk').click(function () {
    $('.popup__bg__menu').fadeOut(); (600);
    $('html').removeClass('no-scroll');
});

$('.cv1').click(function () {
    if ( $("#block1").hasClass("KL") ) {
        $("#block1").removeClass("KL"); 
        $("#block2").addClass("KL");   
        $("#block3").addClass("KL");  
        $("#block4").addClass("KL");  
        $("#block5").addClass("KL");  
        $("#block6").addClass("KL");  
    }
    else{
        $("#block1").addClass("KL");  
    }
});
$('.cv2').click(function () {
    if ( $("#block2").hasClass("KL") ) {
        $("#block2").removeClass("KL"); 
        $("#block1").addClass("KL");   
        $("#block3").addClass("KL");  
        $("#block4").addClass("KL");  
        $("#block5").addClass("KL");  
        $("#block6").addClass("KL");  
    }
    else{
        $("#block2").addClass("KL");
    }
});
$('.cv3').click(function () {
    if ( $("#block3").hasClass("KL") ) {
        $("#block3").removeClass("KL");
        $("#block1").addClass("KL");   
        $("#block2").addClass("KL");  
        $("#block4").addClass("KL");  
        $("#block5").addClass("KL");  
        $("#block6").addClass("KL");   
    }
    else{
        $("#block3").addClass("KL");  
    }
});
$('.cv4').click(function () {
    if ( $("#block4").hasClass("KL") ) {
        $("#block4").removeClass("KL");
        $("#block1").addClass("KL");   
        $("#block3").addClass("KL");  
        $("#block2").addClass("KL");  
        $("#block5").addClass("KL");  
        $("#block6").addClass("KL");   
    }
    else{
        $("#block4").addClass("KL");  
    }
});
$('.cv5').click(function () {
    if ( $("#block5").hasClass("KL") ) {
        $("#block5").removeClass("KL");
        $("#block1").addClass("KL");   
        $("#block3").addClass("KL");  
        $("#block4").addClass("KL");  
        $("#block2").addClass("KL");  
        $("#block6").addClass("KL");   
    }
    else{
        $("#block5").addClass("KL");  
    }
});
$('.cv6').click(function () {
    if ( $("#block6").hasClass("KL") ) {
        $("#block6").removeClass("KL");
        $("#block1").addClass("KL");   
        $("#block3").addClass("KL");  
        $("#block4").addClass("KL");  
        $("#block5").addClass("KL");  
        $("#block2").addClass("KL");  
    }
    else{
        $("#block6").addClass("KL");  
    }
});


$('.open__popup__sher').click(function (e) {
    $('body,html').animate({ scrollTop: 0 }, 400);
    e.preventDefault();
    $('.popup__bg__find').fadeIn(600);
    $('html').addClass('no-scroll');
});

$('.close__popup__find').click(function () {
    $('.popup__bg__find').fadeOut(); (600);
    $('html').removeClass('no-scroll');
});





$('.vrs__open').click(function () {
    // $('.popup__bg__find').fadeOut(); (600);
    // $('html').removeClass('no-scroll');
    $('body').css({
        'filter':'gray',
        '-webkit-filter':'grayscale(100%)'
      });
    $('.top__info__stl').css({
        'display':'none',
      });
});
