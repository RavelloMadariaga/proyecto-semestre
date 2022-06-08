function agregarTabla() {
    var user = document.getElementById("user").value;
    var pass = document.getElementById("pass").value;
    var type = document.getElementById("slcTipo").value;
    var table = document.getElementById("bodyTabla1");
    var tab = document.getElementById("tabla1").rows.length; 
    var row = table.insertRow(0);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    cell1.innerHTML = user;
    cell2.innerHTML = pass;
    cell3.innerHTML = type;
    cell4.innerHTML = '<button type="button" class="btn btn-danger" onclick="deleteRow(this)">Eliminar</button>';
    if(tab>0){
        document.getElementById("tabla1").style.visibility="visible";
    }
}

function deleteRow(r) {
    var i = r.parentNode.parentNode.rowIndex;
    document.getElementById("tabla1").deleteRow(i);
    
    var tab = document.getElementById("bodyTabla1").rows.length; 
    if(tab<=0){
        document.getElementById("tabla1").style.visibility="hidden";
    }
}  