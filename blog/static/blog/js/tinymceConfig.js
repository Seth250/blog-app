tinymce.init({
    height: 480,
    width: 960,
    theme: 'silver',
    selector: '.form-content',
    plugins: [
        'emoticons template save link image media preview codesample',
        'advlist table code lists fullscreen insertdatetime nonbreaking textpattern',
        'directionality searchreplace wordcount visualblocks toc print',
        'visualchars paste fullscreen autolink imagetools charmap hr anchor pagebreak'
    ],
    toolbar1: 
        `fullscreen preview bold italic underline | fontselect fontsizeselect  | forecolor backcolor | 
        alignleft alignright | aligncenter alignjustify | indent outdent | bullist numlist table | link image media | 
        codesample`,
    image_advtab: true
});