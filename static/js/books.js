$(document).on('click', '.btnDelete', function(){
    if (confirm("Are you sure to delete?") == true){
        const bookId = $(this).attr('data-row')
        location.href = `/books/${bookId}/delete`
    }
})