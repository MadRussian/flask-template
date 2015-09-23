/*
 * Given a url attach the $SCRIPT_ROOT to it
 */
function get_script_url(url)
{
  if(url == null) {
    return;
  }
  return $SCRIPT_ROOT + url;
}

/*
 * Navigation bars can overlap with the main content. This attempts to fix this
 * because another approach has not been found. Essentially go through the
 * navigations in the #wrap_navs and get a sum of the navs inside. Also for
 * each nav within the #wrap_navs it sets its margin top as well.
 */
function fix_navbars()
{
  var navbar_height = 0;
  var extra = 10;
  $.each($("#wrap_navs .navbar"), function(ix, div) {
    $(div).css('margin-top', navbar_height);
    navbar_height += $(div).height();
  });
  var total = navbar_height + extra;
  $('.page-content').css('margin-top', total);
}

function fix_icons()
{
  $(".fa").hide();
  $(".fa").show();
}

$(document).ready(function() {
  setTimeout(fix_icons, 10);
  // Fix navbar height
  fix_navbars();
  $(window).resize(fix_navbars);
  
  // Setup tooltips
  $(document).tooltip({
    show: { delay: 600 },
    limit: true,
  });

  // Setup secondary tabs
  if(page_data['tab'] != null) {
    $(sprintf("li#%s", page_data['tab'])).addClass("active");
  }
  fix_icons();
});
