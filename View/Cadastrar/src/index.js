function Cadastrar(){
  var email = document.getElementsByTagName('input')[0]
  var nome = document.getElementsByTagName('input')[1]
  var nascimento = document.getElementsByTagName('input')[2]
  var alerta_nasc = document.getElementsByTagName('p')[0]
  var alerta_senha = document.getElementsByTagName('p')[1]
  var alerta_senha02 = document.getElementsByTagName('p')[2]
  var senha = document.getElementsByTagName('input')[3]
  var senha_02 = document.getElementsByTagName('input')[4]
  const data_atual = new Date()


  //
  var caracteres = String(nascimento.value)
  var data = ""
  for (i=0; i < 4; i++){
    data += caracteres[i]
  }
  //alert(data)
  data = Number.parseInt(data)

  //Quantidade de caixas preenchidas corretamente
  let form = [false, false, false]
  
  if (email.value.length == 0){
    email.style.borderColor = "RED"
    form[0] = false
  } 
  else{
    email.style.borderColor = "GRAY"
    form[0] = true
  }

  if (nome.value.length == 0){
    nome.style.borderColor = "RED"
    form[1] = false
  }
  else{
    nome.style.borderColor = "GRAY"
    form[1] = true
  }


  if (nascimento.value.length == 0 || data <= 1900 || data > (data_atual.getFullYear() - 18)){
    nascimento.style.borderColor = "RED"
    alerta_nasc.style.display = "block"
    nascimento.style.marginTop = "2px"
    form[2] = false
    
  }

  else{
    nascimento.style.borderColor = "GRAY"
    alerta_nasc.style.display = "none"
    nascimento.style.marginTop = "20px"
    form[2] = true
  }


  // No minimo 5 caracteres para a senha
  if (senha.value.length > 4){
    if (senha.value == senha_02.value){
      senha.style.borderColor = "GRAY"
      senha_02.style.borderColor = "GRAY"
      senha.style.marginTop = "20px"
      senha_02.style.marginTop = "20px"
      alerta_senha02.style.display = "none"
      alerta_senha.style.display = "none"


      if (form[0] && form[1] && form[2] ){
        Solicitacao(String(email.value), String(nome.value), String(nascimento.value), String(senha.value))
      }
    }
    else{
      senha.style.borderColor = "RED"
      alerta_senha.style.display = "none"
      senha.style.marginTop = "20px"
      senha_02.style.borderColor = "RED"
      alerta_senha02.style.display = "block"
      senha_02.style.marginTop = "2px"
    }
    
  }
  else{
    alerta_senha.style.display = "block"
    senha.style.marginTop = "2px"
    senha.style.borderColor = "RED"
    senha_02.style.borderColor = "RED"

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