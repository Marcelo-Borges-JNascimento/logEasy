console.log('Olá mundo!')

let botao_salvar = document.getElementById('botao_salvar')
const botao_redirect = document.getElementById('botao_redirect')
const campo_nome = document.getElementById('id_nome_produto')
const codigo = document.getElementById('id_codigo')
const quantidade = document.getElementById('id_quantidade')

const form_enviado = () => {
    window.alert('O produto foi registrado!')
}


// Função que valida se o nome do produto foi registrado no input
const valida = () => {
    if (campo_nome.value == '' ) {
        console.log('vazio')
    }
    else {
        console.log(campo_nome.value)
        if (codigo.value && quantidade.value != 0 && botao_salvar.type != 'button') {
            //Evento que dispara um alert para informar que o produto foi registrado
            botao_salvar.type = 'submit'
            botao_salvar.addEventListener('click', form_enviado)
        }
        else{
            botao_salvar.type = 'submit'
            console.log('Código e quantidade não podem ter o valor zerado!')
        }
    }
}



campo_nome.addEventListener('input', valida)
codigo.addEventListener('input', valida)
quantidade.addEventListener('input', valida)
