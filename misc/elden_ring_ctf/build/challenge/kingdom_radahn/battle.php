<?php
// PHP code to handle form submission and validation
$message = '';
$success = false;

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $password = $_POST['password'];

    // Check if the entered password matches the secret message
    if ($password == 'Starscourge_Radahn') {
        $success = true;
        $message = 'Congratulations! You have defeated Radahn.';
    } else {
        $message = 'Incorrect message. Try again!';
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Starscourge Radahn's Challenge</title>
 <h1>Starscourge Radahn</h1>
  <img id="radahn-image" src="../static/images/radahn.jpg" alt="Radahn">
  <p>To defeat Radahn, find the hidden message inside the image.</p>
    <style>
        body {
            background-color: #8B0000; /* Dark Red */
      	    color: white;
            font-family: Arial, sans-serif;
            text-align: center;
	    margin: 0;
      	    padding: 0;
        }
        h1 {
            color: #FF6347;
        }
        #message {
            margin-top: 20px;
        }
        .success {
            color: green;
        }
        .error {
            color: red;
        }
        .hint {
            color: orange;
            font-weight: bold;
        }
        .image-container {
            margin: 20px 0;
        }
        img {
            max-width: 80%;
            height: auto;
        }
    </style>
</head>
<body>

    <h1>Starscourge Radahn's Challenge</h1>

    <div class="image-container">
        <img src="static/images/radahn.jpg" alt="Radahn">
    </div>

    <p>Welcome to Radahn's domain! To proceed, you must uncover the hidden secret in Radahn's image.</p>

    <!-- Form to enter the password -->
    <form method="POST" action="">
        <label for="password">Enter the secret message:</label>
        <input type="text" id="password" name="password" required>
        <button type="submit">Submit</button>
    </form>

    <!-- Display the result message based on the validation -->
    <div id="message">
        <?php if ($message): ?>
            <p class="<?php echo $success ? 'success' : 'error'; ?>"><?php echo $message; ?></p>
        <?php endif; ?>
        
        <!-- Show hint if the password is correct -->
        <?php if ($success): ?>
            <p class="hint">Hint: Radahn has fallen, but the next challenge awaits you. Proceed to the next kingdom.</p>
        <?php endif; ?>
    </div>

</body>
</html>
