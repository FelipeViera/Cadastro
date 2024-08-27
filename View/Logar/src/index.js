function Logar(){
    var email = document.getElementsByTagName('input')[0]
    var senha = document.getElementsByTagName('input')[1]
    var alerta = document.getElementsByTagName('p')[0]
    var c_email = email.value.length
    var c_senha = senha.value.length
    var verificacao = [2]

    if (c_email > 0){
      verificacao[0] = true
    }

    else{
      verificacao[0] = false
      
    }

    if (c_senha > 0){
      verificacao[1] = true
    }

    else {
      verificacao[1] = false
    }

    if (verificacao[0] && verificacao[1]){
        Solicitacao(String(senha.value), String(email.value))
    }
    else{
      senha.style.borderColor = "red"
      email.style.borderColor = "red"
      alerta.style.display ="block"

    }
    
}

async function Solicitacao(valor, valor2) {
    //Realizar a solicitação
    link = 'http://localhost:5000/login'

    var login = {
      email: valor2,
      senha: valor,
    }

    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ senha: valor, email: valor2 }), // Substitua o valor conforme necessário
      })
      
      .then(response => response.json())
      .then(data => {
        console.log(data.resultado), Salvar(data, login)
    })
      .catch((error) => console.error('Erro:', error));;
      
     
  }

function Salvar(data, login){
    if (String(data.resultado) == 'ACEITO'){
      localStorage.setItem("login", JSON.stringify(login))
      window.location.href = "./../../View/Perfil/index.html"
    }
    else{

      if (String(data.resultado) == 'NEGADO'){
        alert('login Inválido')
      }
      
      
    }
    

  }