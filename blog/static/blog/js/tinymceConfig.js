tinymce.init({
    height: 480,
    width: 960,
    selector: 'textarea',
    plugins: [
        'emoticons template textcolor save link image media preview codesample contextmenu',
        'advlist table code lists fullscreen insertdatetime nonbreaking textpattern',
        'contextmenu directionality searchreplace wordcount visualblocks textcolor toc',
        'visualchars paste fullscreen autolink imagetools charmap print hr anchor pagebreak'
    ],
    toolbar1: 
        `fullscreen preview bold italic underline | fontselect fontsizeselect  | forecolor backcolor | 
        alignleft alignright | aligncenter alignjustify | indent outdent | bullist numlist table | link image media | 
        codesample`,
    image_advtab: true
});