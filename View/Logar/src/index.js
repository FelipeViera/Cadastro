function Logar(){
    var email = document.getElementsByTagName('input')[0]
    var senha = document.getElementsByTagName('input')[1]
    var c_email = email.value.length
    var c_senha = senha.value.length
    if (c_email > 0 && c_senha > 0){
        Solicitacao(String(senha.value), String(email.value))
    }
    
}

async function Solicitacao(valor, valor2) {
    //Realizar a solicitação
    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ senha: valor, email: valor2 }), // Substitua o valor conforme necessário
      })
      
      .then(response => response.json())
      .then(data => {
        console.log(data), alert(data.resultado)
    })
      .catch((error) => console.error('Erro:', error));
     
  }