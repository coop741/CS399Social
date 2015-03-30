/*
 Click listener for form submit in navbar
*/

$("#submitMood").click(function() {
    $("submitMood").blur();
    postMoods($("#mood-input").val(), function(response) {
        $('#moodModal').modal('hide');
    });
});

$("#submitMood2").click(function() {
    $("submitMood2").blur();
    postMoods($("#mood-input-2").val(), function(response) {
        // do something
    });
});

function postMoods(data, callback) {
    $.post("/mood", {
            csrfmiddlewaretoken: csrf_token,
            data: JSON.stringify(data)
        },
        function(response) {
            console.log(response);
            if (callback) {
                callback(response);
            }
        }
    );
}
function getMoods(username) {
    var url = "/mood";
    if (username) {
        url = url + '?username=' + username;
    }
    $.get(url, function (data) {
        $('.moods').empty();
        console.log(data);
        $.each(data, function (index, value) {
            $('<div class="alert alert-info"/>').html(value.fields.description).appendTo('.moods');
        });
    });
}
