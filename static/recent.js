function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function showUpvote() {
    plotsId = getCookie('upvoted');
    plotsId = plotsId.replace(/['"]+/g, '');
    plotsIdTable = plotsId.split(" ");
    if (typeof plotsIdTable !== 'undefined' && !(plotsIdTable.includes(''))) {
        var i = 0;
        for (i = 0; i < plotsIdTable.length; i++) {
            $(".vote[id="+ plotsIdTable[i] +"]").toggleClass("on");
        };
    };
};


$(function() {
    var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
    
    showUpvote();
    
    $(".vote").click(function() {
        var dataId = $(this).attr("id");
        $.ajax({
            type: 'POST',
            url: '/' + dataId + '/upvote/',
            data: {
                csrfmiddlewaretoken: csrfToken,
                id: dataId
            },
            success: function () {
                $(".vote[id="+ dataId +"]").toggleClass("on");
                $("p[id="+ dataId +"]").load(" p[id="+ dataId +"] ");
            }
        });
    });
});
