<?php
// Define the correct password
$correct_password = "Malenia_password";
$response = ""; // This will store the feedback message

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $password = $_POST["password"];

    if ($password === $correct_password) {
        // Success message when Malenia is defeated
        $response = "<p style='color: green;'>Malenia, Blade of Miquella, has been defeated!</p>";
        $response .= "<p style='color: orange;'>Hint: Radahn awaits you. Search his battlefield for hidden paths.</p>";
    } else {
        // Failure message for incorrect passwords
        $response = "<p style='color: red;'>You are not worthy to defeat Malenia. Try again!</p>";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Malenia's Domain</title>
  <link rel="stylesheet" type="text/css" href="/static/css/styles.css">
</head>
<body>
  <h1>Malenia, Blade of Miquella</h1>
  <img src="/static/images/malenia.jpg" alt="Malenia" style="width:50%; height:auto;">
  <p>To defeat me, you must unlock the code to the secret chamber.</p>
  
  <form method="POST" action="">
    <label for="password">Enter the password:</label>
    <input type="text" id="password" name="password" required>
    <button class="button" type="submit">Submit</button>
  </form>

  <!-- Display feedback message -->
  <div id="response">
    <?php echo $response; ?>
  </div>

  <!-- Include JavaScript file -->
  <script src="/kingdom_malenia/vulnerability.js"></script>
</body>
</html>

