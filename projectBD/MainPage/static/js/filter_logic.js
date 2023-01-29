var select = $('#brand-select');

select.on('change', function() {
    var selectedValue = $(this).val();
    $.ajax({
        type: 'GET',
        url: '/',
        data: {brand: selectedValue},
        success: function(data) {
        console.log("dzialam")
            var modelSelect = $('#model-select');
            modelSelect.empty();
            $.each(data.models, function(index, model) {
                modelSelect.append($('<option>', {
                    value: model[0],
                    text: model[0]
                }));
            });
        }
    });
});
