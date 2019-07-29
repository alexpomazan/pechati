$(document).ready(function () {
    $('nav').removeClass("default");
    $(window).scroll(function () {
        if ($(this).scrollTop() > 20)
            $('nav').addClass("default").fadeIn('fast');
        else
            $('nav').removeClass("default").fadeIn('fast');

    var wrap = $('#wrapper'),
        btn = $('.open-modal-btn'),
        modal = $('.cover, .modal, .content');

    btn.on('click', function () {
        modal.fadeIn();
    });

// close modal
    $('.modal').click(function () {
        wrap.on('click', function (event) {
            var select = $('.content');
            if ($(event.target).closest(select).length)
                return;
            modal.fadeOut();
            wrap.unbind('click');
        });
    });

    })

});
// open modal