console.log('Encurtador de url pronto!');

function copiar() {
    var txt = document.getElementById('novo-link');
    txt.select();
    document.execCommand('copy');
    M.toast({html: 'Copiado!'})
}