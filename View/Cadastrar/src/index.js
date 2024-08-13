function Cadastrar(){
  var email = document.getElementsByTagName('input')[0].value
  var nome = document.getElementsByTagName('input')[1].value
  var nascimento = document.getElementsByTagName('input')[2].value
  var senha = document.getElementsByTagName('input')[3].value
  

  if (email.length > 0 && nome.length > 0 && nascimento.length > 0 && senha.length > 0){
    Solicitacao(String(email), String(nome), String(nascimento), String(senha))
  }

}

async function Solicitacao(valor1, valor2, valor3, valor4) {
  //Realizar a solicitação
  fetch('http://localhost:5000/cadastro', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email: valor1, nome: valor2, nascimento: valor3, senha: valor4}), // Substitua o valor conforme necessário
    })
    
    .then(response => response.json())
    .then(data => {
      console.log(data), next_pagina(data)
  })
    .catch((error) => console.error('Erro:', error));
   
}

function next_pagina(data){
  if (String(data.resultado) == 'CADASTRADO'){
    window.location.href = "./../../View/Logar/index.html"
  }
  else{
    alert('Tente outro e-mail')
  }
  

}