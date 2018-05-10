$(document).ready(function() {
    $("#do_generate_sentence").click(function(event) {
        event.preventDefault();
        $.post('/generate', $("#generated_sentence_form").serialize(), function(data, textStatus, xhr) {
            $("#generated_sentence").html(data);
        });
    });

    $("#do_randomize_words").click(function(event) {
        $.post('/randomize_words', function(data, textStatus, xhr) {
            $("#keywords").val(data);
            $("#do_generate_sentence").click();
        });
    });

    $("#do_randomize_words").click();
    $("#do_generate_sentence").click();
});
