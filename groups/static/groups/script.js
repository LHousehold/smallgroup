$(document).ready(function() {

  $(".redirect_btn").click(function() {
    var origin =  window.location.origin;
    var src = event.target;
    var group_type = src.getAttribute("data-group_type")
    window.location = origin + "/groups/?t=" + group_type
  })

  $("#submit_signup_form").click(function() {
    //attempt to send email, probably with some kind of ajax thing...
    //

    // redirect to thank you page if successful
    var origin =  window.location.origin;
    window.location = origin + "/thankyou"
  })

  $(".group_sign_up_btn").click(function() {
    var origin =  window.location.origin;
    var src = event.target;
    var group_id = src.getAttribute("data-group_id")
    window.location = origin + "/signup/?id=" + group_id
  })

  $('.navbar a').click(function(e){
    $('html, body').animate({
        scrollTop: $( $.attr(this, 'href') ).offset().top
    }, 500);
    $('.navbar li.active').removeClass('active');
    var $this = $(this);
    if (!$this.hasClass('active')) {
      $this.parent().addClass('active');
    }
    e.preventDefault();
    return false;
  });

})
