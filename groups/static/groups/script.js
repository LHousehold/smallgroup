$(document).ready(function() {

  $(".redirect_btn").click(function() {
    var origin =  window.location.origin;
    var src = event.target;
    var group_type = src.getAttribute("data-group_type")
    window.location = origin + "/groups?t=" + group_type
  })

})

