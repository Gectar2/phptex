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
    if ($("#block1").hasClass("KL")) {
        $("#block1").removeClass("KL");
        $("#block2").addClass("KL");
        $("#block3").addClass("KL");
        $("#block4").addClass("KL");
        $("#block5").addClass("KL");
        $("#block6").addClass("KL");
    }
    else {
        $("#block1").addClass("KL");
    }
});
$('.cv2').click(function () {
    if ($("#block2").hasClass("KL")) {
        $("#block2").removeClass("KL");
        $("#block1").addClass("KL");
        $("#block3").addClass("KL");
        $("#block4").addClass("KL");
        $("#block5").addClass("KL");
        $("#block6").addClass("KL");
    }
    else {
        $("#block2").addClass("KL");
    }
});
$('.cv3').click(function () {
    if ($("#block3").hasClass("KL")) {
        $("#block3").removeClass("KL");
        $("#block1").addClass("KL");
        $("#block2").addClass("KL");
        $("#block4").addClass("KL");
        $("#block5").addClass("KL");
        $("#block6").addClass("KL");
    }
    else {
        $("#block3").addClass("KL");
    }
});
$('.cv4').click(function () {
    if ($("#block4").hasClass("KL")) {
        $("#block4").removeClass("KL");
        $("#block1").addClass("KL");
        $("#block3").addClass("KL");
        $("#block2").addClass("KL");
        $("#block5").addClass("KL");
        $("#block6").addClass("KL");
    }
    else {
        $("#block4").addClass("KL");
    }
});
$('.cv5').click(function () {
    if ($("#block5").hasClass("KL")) {
        $("#block5").removeClass("KL");
        $("#block1").addClass("KL");
        $("#block3").addClass("KL");
        $("#block4").addClass("KL");
        $("#block2").addClass("KL");
        $("#block6").addClass("KL");
    }
    else {
        $("#block5").addClass("KL");
    }
});
$('.cv6').click(function () {
    if ($("#block6").hasClass("KL")) {
        $("#block6").removeClass("KL");
        $("#block1").addClass("KL");
        $("#block3").addClass("KL");
        $("#block4").addClass("KL");
        $("#block5").addClass("KL");
        $("#block2").addClass("KL");
    }
    else {
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

$('.version__visually__btn').click(function () {
    if ($(".version__visually__btn").hasClass("vrs__open")) {
        $(".version__visually__btn").removeClass("vrs__open");
        $(".version__visually__btn").addClass("vrs__close");

        $('.header__vrs').css({
            'display': 'flex',
        });

        $(".vers__a").text(" ОБЫЧНАЯ ВЕРСИЯ");

        $(".top__info__stl").css({
            'display': 'none',
        });
    }
    else {
        window.parent.location = window.parent.location.href;
        $(".version__visually__btn").removeClass("vrs__close");
        $(".version__visually__btn").addClass("vrs__open");

        $('.header__vrs').css({
            'display': 'none',
        });
        $(".vers__a").text(" ВЕРСИЯ ДЛЯ СЛАБОВИДЯЩИХ");
        if (window.screen.width > 1110){
            $(".display__block__right").css({
                'display': 'flex',
            });
            $(".display__block__left").css({
                'width': `${window.screen.width-5}px`,
            });
            $(".top__info__stl").css({
                'display': 'flex',
            });
        }
        $(".text__content").css({
            'font-size': '14px',
        });
        $(".title__content").css({
            'font-size': '16px',
        });
        $(".text__end__content").css({
            'font-size': '14px',
        });
        $("body").css({
            'background': '#fff',
        });
        $(".contact-info-adres").css({
            'color': '#000',
        });
        $(".title__college").css({
            'color': '#000',
        });
        $(".global__color").css({
            'color': '#000',
        });
        $(".top__info, .title__news, .contact-info-adres, .text_ministry, .title__end" ).css({
            'letter-spacing': '0',
        });
        $(".title__college").css({
            'letter-spacing': '0',
        });
        $(".title__content").css({
            'letter-spacing': '0',
        });
        $(".text__content").css({
            'letter-spacing': '0',
        });
        $(".text__end__content").css({
            'letter-spacing': '0',
        });
        $(".btn__vl__one").css({
            'letter-spacing': '0',
        });
        $(".btn__vl__two").css({
            'letter-spacing': '0',
        });
        $(".info__line").css({
            'letter-spacing': '0',
        });
        $(".nw").css({
            'letter-spacing': '0',
        });
    }
});


$('.disg__font-siz1').click(function () {
    $(".text__content").css({
        'font-size': '14px',
    });
    $(".contact-info-adres").css({
        'font-size': '16px',
    });
    $(".title__content").css({
        'font-size': '16px',
    });
    $(".text__end__content").css({
        'font-size': '14px',
    });
    $(".nw").css({
        'font-size': '14px',
    });

    $(".display__block__right").css({
        'display': 'flex',
    });
    $(".top__info__stl").css({
        'display': 'flex',
    });
    $(".display__block__left").css({
        'width': '720px',
    });
    $(".btn__vl__one").css({
        'margin-left': '-200px',
    });
});
$('.disg__font-siz2').click(function () {
    $(".text__content").css({
        'font-size': '16px',
    });
    $(".contact-info-adres").css({
        'font-size': '17px',
    });
    $(".title__content").css({
        'font-size': '18px',
    });
    $(".text__end__content").css({
        'font-size': '16px',
    });
    $(".nw").css({
        'font-size': '16px',
    });
    $(".display__block__right").css({
        'display': 'none',
    });
    $(".display__block__left").css({
        'width': '1160px',
    });
});
$('.disg__font-siz3').click(function () {
    $(".text__content, .contact-info-adres").css({
        'font-size': '18px',
    });
    $(".title__content").css({
        'font-size': '20px',
    });
    $(".text__end__content").css({
        'font-size': '18px',
    });
    $(".nw").css({
        'font-size': '18px',
    });
    $(".display__block__right").css({
        'display': 'none',
    });
    $(".display__block__left").css({
        'width': '1160px',
    });
});

$('.disg__font1').click(function () {
    $("body").css({
        'background': 'none',
    });
    $(".contact-info-adres").css({
        'color': '#000000',
    });
    $(".title__college").css({
        'color': '#000000',
    });
    $(".global__color").css({
        'color': '#000',
    });
});
$('.disg__font2').click(function () {
    $("body").css({
        'background': '#252525',
    });
    $(".contact-info-adres").css({
        'color': '#fff',
    });
    $(".title__college").css({
        'color': '#fff',
    });
    $(".global__color").css({
        'color': '#fff',
    });
});
$('.disg__font3').click(function () {
    $("body").css({
        'background': '#9dd1ff',
    });
    $(".contact-info-adres").css({
        'color': '#000000',
    });
    $(".title__college").css({
        'color': '#000000',
    });
    $(".logo_phpro").css({
        'filter': 'gray',
    });
    $(".global__color").css({
        'color': '#000',
    });
});


$('.disg__font-init1').click(function () {
    $(".top__info, .title__news, .contact-info-adres, .text_ministry, .title__end" ).css({
        'letter-spacing': '0',
    });
    $(".title__college").css({
        'letter-spacing': '0',
    });
    $(".title__content").css({
        'letter-spacing': '0',
    });
    $(".text__content").css({
        'letter-spacing': '0',
    });
    $(".text__end__content").css({
        'letter-spacing': '0',
    });
    $(".btn__vl__one").css({
        'letter-spacing': '0',
    });
    $(".btn__vl__two").css({
        'letter-spacing': '0',
    });
    $(".info__line").css({
        'letter-spacing': '0',
    });
    $(".nw").css({
        'letter-spacing': '0',
    });
});
$('.disg__font-init2').click(function () {
    $(".top__info, .title__news, .contact-info-adres, .text_ministry, .title__end" ).css({
        'letter-spacing': '0.5px',
    });
    $(".title__college").css({
        'letter-spacing': '0.5px',
    });
    $(".title__content").css({
        'letter-spacing': '0.5px',
    });
    $(".text__content").css({
        'letter-spacing': '0.5px',
    });
    $(".text__end__content").css({
        'letter-spacing': '0.5px',
    });
    $(".btn__vl__one").css({
        'letter-spacing': '0.5px',
    });
    $(".btn__vl__two").css({
        'letter-spacing': '0.5px',
    });
    $(".info__line").css({
        'letter-spacing': '0.5px',
    });
    $(".nw").css({
        'letter-spacing': '0.5px',
    });
});
$('.disg__font-init3').click(function () {
    $(".top__info, .title__news, .contact-info-adres, .text_ministry, .title__end" ).css({
        'letter-spacing': '1px',
    });
    $(".title__college").css({
        'letter-spacing': '1px',
    });
    $(".title__content").css({
        'letter-spacing': '1px',
    });
    $(".text__content").css({
        'letter-spacing': '1px',
    });
    $(".text__end__content").css({
        'letter-spacing': '1px',
    });
    $(".btn__vl__one").css({
        'letter-spacing': '1px',
    });
    $(".btn__vl__two").css({
        'letter-spacing': '1px',
    });
    $(".info__line").css({
        'letter-spacing': '1px',
    });
    $(".nw").css({
        'letter-spacing': '1px',
    });
});