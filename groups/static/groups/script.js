$(document).ready(function() {

  $(".redirect_btn").click(function() {
    var origin =  window.location.origin;
    var src = event.target;
    var group_type = src.getAttribute("data-group_type")
    window.location = origin + "/groups/?t=" + group_type
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
