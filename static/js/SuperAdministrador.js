function abrirFormulario1(){
    var frm1 = document.form1;
    var frm2= document.form2;
    var frm3= document.form3;

    if(frm1.style.display== "block"){
        frm1.style.display="none";
        frm2.style.display="none";
        frm3.style.display="none";
    }else if(frm1.style.display== "none"){
        frm1.style.display="block";
        frm2.style.display="none";
        frm3.style.display="none";
    }  
}

function abrirFormulario2(){
    var frm1= document.form1;
    var frm2= document.form2;
    var frm3= document.form3;
    if(frm2.style.display=="block"){
        frm2.style.display="none";
        frm1.style.display="none";
        frm3.style.display="none";
    }else if(frm2.style.display== "none"){
        frm2.style.display="block";
        frm1.style.display="none";
        frm3.style.display="none";
    } 
}

function abrirFormulario3(){
    var frm1= document.form1;
    var frm2= document.form2;
    var frm3= document.form3;

    if(frm3.style.display=="block"){
        frm3.style.display="none";
        frm1.style.display="none";
        frm2.style.display="none";
    
    }else if(frm3.style.display== "none"){
        frm3.style.display="block";
        frm2.style.display="none";
        frm1.style.display="none";
    } 
}

function buscarAdministrador(){

}