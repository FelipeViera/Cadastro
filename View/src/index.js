function Logar(){
    var email = document.getElementsByTagName('input')[0]
    var senha = document.getElementsByTagName('input')[1]
    var c_email = email.value.length
    var c_senha = senha.value.length
    if (c_email > 0 && c_senha > 0){
        Solicitacao()
    }
    
}

async function Solicitacao() {
    //Realizar a solicitação
  }