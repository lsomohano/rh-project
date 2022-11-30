var checkState = '';

$('.bulk_action input#check-all').on('ifChecked', function () {
    checkState = 'all';
    countCheckedd();
});
$('.bulk_action input#check-all').on('ifUnchecked', function () {
    checkState = 'none';
    countCheckedd();
});
    
function countCheckedd() {
    if (checkState === 'all') {
        $(".bulk_action input[name='partidas[]']").iCheck('check');
    }
    if (checkState === 'none') {
        $(".bulk_action input[name='partidas[]']").iCheck('uncheck');
    }

    var checkCount = $(".bulk_action input[name='partidas[]']:checked").length;

    if (checkCount) {
        $('.column-title').hide();
        $('.bulk-actions').show();
        $('.action-cnt').html(checkCount + ' Records Selected');
    } else {
        $('.column-title').show();
        $('.bulk-actions').hide();
    }
}  