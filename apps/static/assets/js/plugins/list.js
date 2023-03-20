$(function() {
    edit = $('.edit');

    getData();

    $('#data tbody').on('click', '.editarPerfil', function () {
        edit.find('span').html('Editar perfil');
        edit.find('i').removeClass().addClass('fas fa-edit');

        var tr = tblUser.cell($(this).closest('td, li')).index();
        var data = tblUser.row(tr.row).data();
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="username"]').val(data.username);
        $('input[name="email"]').val(data.email);
        $('input[name="password"]').val(data.password);
        $('input[name="first_name"]').val(data.first_name);
        $('input[name="last_name"]').val(data.last_name);
        $('input[name="unidad"]').val(data.unidad);
        $('input[name="claveClues"]').val(data.claveclues);
        $('input[name="jurisdiccion"]').val(data.jurisdiccion);
        $('input[name="municipio"]').val(data.municipio);
        $('input[name="entidad"]').val(data.entidad);
        $('input[name="groups"]').val(data.groups);
        $('#User').modal('show');
    });
});
