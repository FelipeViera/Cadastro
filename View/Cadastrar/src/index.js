function Cadastrar(){
    var email = document.getElementsByTagName('input')[0]
    var nome = document.getElementsByTagName('input')[1]
    var idade = document.getElementsByTagName('input')[2]
    var senha = document.getElementsByTagName('input')[3]

    var c_email = email.value.length
    var c_senha = senha.value.length
    var c_nome = nome.value.length
    var c_idade = idade.value.length
    if (c_email > 0 && c_senha > 0 && c_nome > 0 && Number(idade.value) > 0){
        //Converter a idade em número
        alert('KO')
    }
    
}
