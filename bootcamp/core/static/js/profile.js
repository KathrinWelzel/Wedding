$(function () {

  $(".follow").click(function () {
    var span = $(this);
    var page_user = $(this).closest(".profile").attr("profile-id");
    var csrf = $("input[name='csrfmiddlewaretoken']", $(this).closest(".page-header")).val();

    $.ajax({
      url: '/follow/user/',
      data: {
        'page_user_id': 3,
        'csrfmiddlewaretoken': csrf
      },
      type: 'post',
      cache: false,
      success: function (data) {
        if ($(span).hasClass("following")) {
          $(span).removeClass("glyphicon-star")
            .removeClass("following")
            .addClass("glyphicon-star-empty");
        }
        else {
          $(span).removeClass("glyphicon-star-empty")
            .addClass("glyphicon-star")
            .addClass("following");
        }
        // TODO $(".follow-count").text(data);
      }
    });

  });

});
