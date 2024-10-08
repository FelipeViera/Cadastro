
try{
  const getLogin = localStorage.getItem("login")
  const loginObject = JSON.parse(getLogin)
  Solicitacao(loginObject)
}
catch(error){
   window.location.href ="./../../View/Logar/index.html"
}





async function Solicitacao(loginObject) {
    //Realizar a solicitação
    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ senha: loginObject.senha, email: loginObject.email }), // Substitua o valor conforme necessário
      })
      
      .then(response => response.json())
      .then(data => {
        console.log(data), Verificar(data.resultado, loginObject)
    })
      .catch((error) => console.error('Erro:', error));
     
  }

function Verificar(valor, loginObject){
    if (String(valor) != "ACEITO"){
      window.location.href = "./../../View/Logar/index.html"
    }
    else{
      Solicitar_dados(loginObject)
    }
}


async function Solicitar_dados(loginObject) {
  //Realizar a solicitação
  fetch('http://localhost:5000/perfil', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({email: loginObject.email, senha: loginObject.senha}), // Substitua o valor conforme necessário
    })


    .then(response => response.json())
    .then(data => {
      console.log(data), Exibir(data, loginObject)
  })
    .catch((error) => console.error('Erro:', error));
   
}

function Exibir(data, loginObject){
  if (String(data.resultado) == "Aceito"){
    var nome = document.getElementById("nome")
    var data_nasc = document.getElementById("data_nasc")
    var email = document.getElementById("email")

    nome.innerText = String(data.nome)

    data_nasc.innerText = "Data de Nascimento: " + String(data.data_nasc)
    email.innerText = "E-mail: " + String(loginObject.email)
    
  }
}


function Excluir(){
  var painel = document.getElementById("painel_excluir")
  painel.style.display = 'grid'
}

function Cancelar(){
  var painel = document.getElementById("painel_excluir")
  painel.style.display = 'none'
}

async function Confirmar(){
  var senha = document.getElementById('caixa-senha').value
  const getLogin = localStorage.getItem("login")
  const loginObject = JSON.parse(getLogin)


  link = 'http://localhost:5000/excluir'

    fetch('http://localhost:5000/excluir', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ senha: String(senha), email: String(loginObject.email)}), // Substitua o valor conforme necessário
      })
      
      .then(response => response.json())
      .then(data => {
        console.log(data.resultado); perfilExcluido(data.resultado);
    })
      .catch((error) => console.error('Erro:', error));;
}

function perfilExcluido(valor){
  var texto = document.getElementsByTagName('p')[0]
  texto.innerText = valor
  if (texto.innerText == "Perfil Excluido"){
    setTimeout(function() {
      alert("A página será recarregada em 5 segundos.");
      window.location.reload();
    }, 5000);
  }
  

}