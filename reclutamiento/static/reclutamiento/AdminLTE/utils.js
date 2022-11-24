/*
  * 
  *Carga una pagina en un div
  *
  */
function cargaModal(metodo, div){
    $.ajax({
        type: "GET",
        url: metodo,
        success: function(html){
            $("#"+div).html(html);
        }
    });
};

/**
 * Carga de Data Teblet
 * 
 * 
 */
function cargaDataTablet(div){
    $('#'+div).DataTable({
        "paging": true,
        "lengthChange": false,
        "searching": true,
        "ordering": true,
        "info": true,
        "autoWidth": false,
        "responsive": true,
        "dom": "<'row'<'col-md-6 col-xs-12'B><'col-md-6 col-xs-12'f>>" +
            /*"<'row'<'col-lg' B > >"+*/
            "<'row'<'col-md-12'tr>>" +
            "<'row'<'col-md-3 col-xs-12'i><'col-md-9 col-xs-12'p>>",
        "buttons": [
            'copy', 'csv', 'excel', 'pdf'
        ]
    });
}

//Initialize Select2 Elements
$(function () {
    $('.select2bs4').select2({
        theme: 'bootstrap4'
    })
})

//---Inicia Cambia valor max de staff autorizado -----//
function calcula_max(){
    var staf_requerido = $('#id_staf_requerido').val();
    var staf_contratado = $('#id_staf_contratado').val();
    return staf_requerido - staf_contratado
}

  //Se inicializa y se modifica el valor max 
$('#id_staf_autorizado').attr({'max': calcula_max()})

$("#id_staf_contratado").change(function(){
    $('#id_staf_autorizado').attr({'max': calcula_max()})
});

$("#id_staf_requerido").change(function(){
    $('#id_staf_autorizado').attr({'max': calcula_max()})
});


/**
 * 
 * Calendarios  Date picker
 */
function calendar(input_id){
    $('#'+input_id).datetimepicker({
        format: 'YYYY-MM-DD'
    });
}


/**
 * 
 * Horarios  Date picker
 */
function timespiker(input_id){
    $('#'+input_id).datetimepicker({
        format: 'HH:mm'
    });
}