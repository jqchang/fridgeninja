$(document).ready( function() {
  $('#addingr').keyup( function() {
    if($(this).val().length > 0) {
      var ingr_list = $.get("/myfridge/"+$(this).val()+"/ingr_json", function(){
        var autocomplete = "<ul>";
        for (ingr in ingr_list.responseJSON) {
          autocomplete += `<li><span>${ingr_list.responseJSON[ingr].name}</span></li>`;
        }
        autocomplete += "</ul>";
        $('.autocomplete').html(autocomplete);
      });
    }
  });
  $(document).on("click", ".autocomplete li", function() {
    alert("Hello world!");
  });
});
