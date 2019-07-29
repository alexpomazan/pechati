$(document).ready(function () {
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
   $(window).resize(function() {
    if ($(window).width() < 768) {
     $('.img-paydeliv').addClass('center-block');
    }
    else {$('.img-paydeliv').removeClass('center-block');}
 });
});