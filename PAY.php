<?php
// Database connection details
$hostname = "your_database_host";
$username = "your_database_username";
$password = "your_database_password";
$database = "your_database_name";

// Create a connection
$conn = new mysqli($hostname, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve data from the client-side
$data = json_decode(file_get_contents("php://input"));

// Sanitize data (for security, you should use prepared statements)
$cardNumber = $conn->real_escape_string($data->cardNumber);
$cardName = $conn->real_escape_string($data->cardName);
$expirationDate = $conn->real_escape_string($data->expirationDate);
$cvv = $conn->real_escape_string($data->cvv);

// Insert data into the database (replace with your own table structure)
$sql = "INSERT INTO payments (card_number, card_name, expiration_date, cvv) 
        VALUES ('$cardNumber', '$cardName', '$expirationDate', '$cvv')";

if ($conn->query($sql) === TRUE) {
    $response = array("message" => "Payment processed successfully.");
} else {
    $response = array("message" => "Error processing payment: " . $conn->error);
}

$conn->close();

// Send a JSON response back to the client
header('Content-Type: application/json');
echo json_encode($response);
?>
