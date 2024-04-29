<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Reemplace 'info@almarosa.es' con su dirección de correo electrónico real
    $receiving_email_address = 'info@almarosa.es';

    // Verificar si los campos requeridos están presentes
    if (isset($_POST['name']) && isset($_POST['email']) && isset($_POST['subject']) && isset($_POST['Mensaje'])) {
        $name = $_POST['name'];
        $email = $_POST['email'];
        $subject = $_POST['subject'];
        $message = $_POST['Mensaje'];

        // Procesar datos y enviar correo electrónico
        $to = $receiving_email_address;
        $subject = "Nuevo mensaje de $name: $subject";
        $body = "Nombre: $name\nCorreo electrónico: $email\nAsunto: $subject\nMensaje:\n$message";

        // Envío de correo electrónico
        if (mail($to, $subject, $body)) {
            echo json_encode(array('status' => 'success', 'message' => 'Su mensaje fue enviado, muchas gracias.'));
        } else {
            echo json_encode(array('status' => 'error', 'message' => 'Error al enviar el mensaje. Por favor, inténtelo de nuevo.'));
        }
    } else {
        echo json_encode(array('status' => 'error', 'message' => 'Todos los campos son requeridos.'));
    }
} else {
    echo json_encode(array('status' => 'error', 'message' => 'El método de solicitud no es válido.'));
}
?>
