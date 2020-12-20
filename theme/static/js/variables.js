$(document).ready(function(){
  $('[id=plus]').on("click", function() {
      let variableFields = $("#variable").clone();
      variableFields.find("#plus").remove();
      variableFields.find("#minus").remove();
      variableFields.find(":input").val('');
      $('[id=new-vars]:last').after(variableFields);
      $('[id=variable]:last').after($('#new-vars').clone());
  });

  $('[id=minus]').on("click", function() {
      if ($('[id=variable]').length > 1) {
        $('[id=variable]:last').remove();
      }
  });
});

