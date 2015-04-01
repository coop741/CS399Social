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
            $('#moodModal').modal('hide');

        }
    );
});


function getMoods(username) {
    var url = "/mood";
    if (username) {
        url = url + '?username=' + username;
    }
    $.get(url, function (data) {
        console.log(data);
        $.get('/static/main/templates/moods.mst', function (template) {
            Mustache.parse(template);
            var rendered = Mustache.render(template, {moods: data});
            $('.moods').html(rendered);
        });
    });
}
