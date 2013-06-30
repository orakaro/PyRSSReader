$(document).on("click", ".unsubcribe", function () {
     var feedName= $(this).data('id');
     $(".modal-body #feedName").val(feedName);
     $(".modal-body #unsubcribe_confirm").text('Do you really want to unsubcribe '+feedName+' ?');
});

$(function(){
$('[rel=star]').tooltip()
});

