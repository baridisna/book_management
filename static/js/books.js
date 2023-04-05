// $(document).ready(function () {
//     $("#id_title").change(function () {
//         alert("The text has been changed.");
//     });
// });

$(document).on('click', '.btnDelete', function () {
    if (confirm("Are you sure to delete?") == true) {
        const bookId = $(this).attr('data-row')
        location.href = `/books/${bookId}/delete`
    }
})

const slugify = str =>
    str
    .toLowerCase().trim()
    .replace(/[^\w\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');

$(document).on('click', '#id_title', function () {
    $(this).change(function(){
        $('#id_slug').val(slugify( this.value ));
    })
})