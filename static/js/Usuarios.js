document.formularioGestionHabitaciones.style.display = "none";

function mostrarPanelGestionarHabitaciones() {
    document.panelReservaciones.style.display = "none";
    document.panelHoteles.style.display = "none";
    document.panelGaleria.style.display = "none";
    document.formularioGestionHabitaciones.style.display = "block";
}

function mostrarPanelDeGalerias() {
    document.panelReservaciones.style.display = "none";
    document.panelHoteles.style.display = "none";
    document.formularioGestionHabitaciones.style.display = "none";
    document.panelGaleria.style.display = "block";
}

function mostrarPanelHoteles() {
    document.panelReservaciones.style.display = "none";
    document.panelGaleria.style.display = "none";
    document.formularioGestionHabitaciones.style.display = "none";
    document.panelHoteles.style.display = "block";

}

function mostrarPanelReservaciones() {
    document.panelGaleria.style.display = "none";
    document.formularioGestionHabitaciones.style.display = "none";
    document.panelHoteles.style.display = "none";
    document.panelReservaciones.style.display = "block";
}

function confirmarComentario() {
    window.prompt("Comentario confirmado");
}