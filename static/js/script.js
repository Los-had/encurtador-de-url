console.log('Encurtador de url pronto!');

function copiar() {
    /*
    var txt = document.querySelector('div.row #link');
    txt.select();
    */
    document.execCommand('copy');
    M.toast({html: 'Copiado!'})
}