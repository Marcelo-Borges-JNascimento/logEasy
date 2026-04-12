
let linha_produto = document.getElementsByTagName('td')
const localizar = document.getElementById('id_localizar')
const botao_localizar = document.getElementById('botao_localizar')



botao_localizar.addEventListener('click', (e) => {

    const texto = localizar.value
    for(let i = 0; i < linha_produto.length; i++){
        nome_prod = linha_produto[i].textContent.trim()
        if(texto == nome_prod){
            console.log(texto)
            linha_produto[i].style.backgroundColor = "aqua"
            setTimeout(() => {
                linha_produto[i].style.backgroundColor = "white"
            }, 1000)
        }
    }   
    
})


