window.addEventListener('DOMContentLoaded', event => {
    //     // Simple-DataTables
    //     // https://github.com/fiduswriter/Simple-DataTables/wiki

    const renderButton = function (data, _cell, _dataIndex, _cellIndex) {
        return `<a href="/users/${data}/edit" class="btn btn-primary">
                    <i class="fa-solid fa-pen-to-square"></i>
                </a>
                <button data-row="${data}" type="button" class="btn btn-danger btnDelete">
                    <i class="fa-solid fa-trash"></i>
                </button>`
    }

    // fetch data
    fetch("/users/data").then(response => response.json()).then(data => {
        if (!data.length) {
            return
        }
        const datatablesSimple = document.getElementById('usersTable');
        new simpleDatatables.DataTable(datatablesSimple, {
            data: {
                data: data
            },
            columns: [
                {
                    select: 6,
                    render: renderButton,
                    type: "number"
                }
            ]
        });
    })
});

$(document).on('click', '.btnDelete', function(){
    if (confirm("Are you sure to delete?") == true){
        const userId = $(this).attr('data-row')
        location.href = `/users/${userId}/delete`
    }
})