/*
 Click listener for form submit in navbar
 */
$("#submitMood").click(function () {
    $("submitMood").blur();
    $.post("/mood", {
            csrfmiddlewaretoken: csrf_token,
            data: JSON.stringify({
                description: $("#mood-input").val()
            })
        },
        function (data) {
            console.log(data);
        }
    );
});

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
