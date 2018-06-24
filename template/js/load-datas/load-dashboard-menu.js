$(document).ready(function() {
    var dashboord = JSON.parse(dashboard_menu);
    for(var i = 0; i < dashboord.menu_platforms.length; i++){
        document.getElementById('REPORT_PLATFORM_NAME').insertAdjacentHTML('beforeend', "<li><a href='index-" + dashboord.menu_platforms[i] + ".html'>"+ dashboord.menu_platforms[i] +"</a></li>")
    }
    
})