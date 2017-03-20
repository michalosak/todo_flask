$("#itemForm").submit(function(event){
    // cancels the form submission
    event.preventDefault();
    submitForm();
});

function submitForm(){

    var add_new_item = $("#add_new_item").val();

    $.ajax({
        type: "POST",
        url: "/ajaxKit/add_item",
        data: "add_new_item=" + add_new_item,
        success : function(response){
            document.getElementById("add_new_item").value = "";
            $("ul").append(response).show();
            $("html, body").animate({ scrollTop: $(document).height() }, "slow");

        }
    });

}

function toggle(toggle_id){

    $.ajax({
        type: "POST",
        url: "/ajaxKit/toggle",
        data: "toggle_id=" + toggle_id,
        success : function(response){
            console.log(response)
            var className = $('#item' + toggle_id).attr('class');

            if (className == "glyphicon glyphicon-unchecked") {
                $('#item' + toggle_id).removeClass('glyphicon glyphicon-unchecked');
                $('#item' + toggle_id).addClass('glyphicon glyphicon-check');
            }
            if (className == "glyphicon glyphicon-check") {
                $('#item' + toggle_id).removeClass('glyphicon glyphicon-check');
                $('#item' + toggle_id).addClass('glyphicon glyphicon-unchecked');

            }
        }
    });

}

function remove(remove_id){

    $.confirm({
        title: 'Please confirm!',
        content: 'Do you really want to delete this item?',
        buttons: {
            Yes: function () {
                $.ajax({
                    type: "POST",
                    url: "/ajaxKit/remove",
                    data: "remove_id=" + remove_id,
                    success : function(response){
                        $('#row' + remove_id).remove();
                        $.alert('Item deleted!');
                    }
                });
            },
            cancel: function () {

            },
        }
    });

}

function edit_item(id) {
    var txt = $("#span"+id).text();
    $.confirm({
        title: '',
        content: '' +
        '<form action="" class="formName">' +
        '<div class="form-group">' +
        '<label>Edit this item</label>' +
        '<textarea placeholder="Update item" class="name form-control" required id="update_item">'+ txt +'</textarea>' +
        '</div>' +
        '</form>',
        buttons: {
            formSubmit: {

                text: 'Update',
                btnClass: 'btn-blue',
                action: function () {

                     $.ajax({
                        type: "POST",
                        url: "/ajaxKit/update",
                        data: "item_id=" + id + "&text_update=" + $('#update_item').val(),
                        success : function(response){
                            $( "#span"+id).replaceWith( response );
                            $.alert('Item udated!');
                        }
                    });
                }

            },
            cancel: function () {
                //close
            },
        },
        onContentReady: function () {
            // bind to events
            var jc = this;
            this.$content.find('form').on('submit', function (e) {
                // if the user submits the form by pressing enter in the field.
                e.preventDefault();
                jc.$$formSubmit.trigger('click'); // reference the button and click it
            });
        }
    });
  };