function visibilizarContrasenia(obj){
    obj= document.getElementById("password");

    if(obj.type=="text"){
        obj.type="password"

    }else if(obj.type=="password"){
        obj.type="text"
    }

}
