/*====== Quantity ========*/
$(document).on('click', '.qtyDec, .qtyInc', function () {
    var $button = $(this);
    numberButtonFunc($button);
});

function numberButtonFunc($button) {
    var oldValue = $button.parent().find("input").val();
    var total = 0;
    $('input[type="text"]').each(function () {
        total += parseInt($(this).val());
    });
    var newVal;
    if ($button.hasClass('qtyInc')) {
        newVal = parseFloat(oldValue) + 1;
    } else {
        if (oldValue > 0) {
            newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 0;
        }
    }
    $button.parent().find("input").val(newVal).trigger('change');
}

$('.gty-container').each(function () {
    var parent = $(this);
    // Adult quantity number
    $('input[name="adult_number"]', parent).change(function () {
        var adults = parseInt($(this).val());
        var html = adults;
        if (typeof adults == 'number') {
            if (adults < 2) {
                html = adults + ' ' + $('.adult', parent).data('text');
            } else {
                html = adults + ' ' + $('.adult', parent).data('text-multi');
            }
        }
        $('.adult', parent).html(html);
    });
    $('input[name="adult_number"]', parent).trigger('change');

    // Children quantity number
    $('input[name="child_number"]', parent).change(function () {
        var children = parseInt($(this).val());
        var html = children;
        if (typeof children == 'number') {
            if (children < 2) {
                html = children + ' ' + $('.children', parent).data('text');
            } else {
                html = children + ' ' + $('.children', parent).data('text-multi');
            }
        }
        $('.children', parent).html(html);
    });
    $('input[name="child_number"]', parent).trigger('change');


});