<?php
// Start session to maintain challenge state
session_start();

// Validation logic for the challenge
function validateSequence($sequence) {
    $correct_sequence = [
        'forefathers',
        'tarnished',
        'grafted'
    ];
    
    foreach ($sequence as $idx => $part) {
        if ($part !== $correct_sequence[$idx]) {
            return false;
        }
    }
    return true;
}

// Handle POST request for form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $sequence = [
        $_POST['hash1'] ?? '',
        $_POST['hash2'] ?? '',
        $_POST['hash3'] ?? ''
    ];
    
    $result = [
        'success' => validateSequence($sequence),
        'message' => validateSequence($sequence) ? 
            'BEAR WITNESS! Password: G0DR1CK_TH3_GR4FT3D' : 
            'Your grafting sequence is wrong. Remember how Godrick starts his speeches...'
    ];
    
    // If it's an AJAX request, return JSON
    if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && 
        strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
        header('Content-Type: application/json');
        echo json_encode($result);
        exit;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Godrick's Grafting Trial</title>
    <style>
        body {
            background-color: #1a0f0f;
            color: #c4a484;
            font-family: 'Cinzel', serif;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
                url('../static/images/godrick.jpg');
            background-size: cover;
            background-position: center;
        }

        .castle-container {
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: rgba(20, 12, 8, 0.9);
            border: 3px solid #8b4513;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(139, 69, 19, 0.5);
        }

        .title {
            text-align: center;
            color: #ffd700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 30px;
        }

        .challenge-section {
            background-color: rgba(30, 18, 12, 0.8);
            padding: 20px;
            margin: 20px 0;
            border: 1px solid #8b4513;
            border-radius: 5px;
        }

        .grafting-input {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            background-color: #2a1810;
            border: 1px solid #8b4513;
            color: #ffd700;
            font-family: 'Courier New', monospace;
        }

        .submit-btn {
            background-color: #8b4513;
            color: #ffd700;
            padding: 12px 24px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-family: 'Cinzel', serif;
            font-weight: bold;
            margin-top: 20px;
            transition: all 0.3s ease;
        }

        .submit-btn:hover {
            background-color: #a0522d;
            transform: scale(1.02);
        }

        .message {
            text-align: center;
            margin: 20px 0;
            padding: 15px;
            border-radius: 4px;
        }

        .error {
            background-color: rgba(139, 0, 0, 0.3);
            border: 1px solid #8b0000;
        }

        .success {
            background-color: rgba(0, 100, 0, 0.3);
            border: 1px solid #006400;
        }

        .hint-box {
            font-style: italic;
            color: #8b4513;
            text-align: center;
            margin: 15px 0;
        }
    </style>
</head>
<body>
    <div class="castle-container">
        <h1 class="title">Godrick's Grafting Trial</h1>
        
        <div class="challenge-section">
            <h2>The Grafting Chamber</h2>
            <p>"Forefathers, one and all... BEAR WITNESS!"</p>
            
            <form method="POST" action="">
                <div class="grafting-input-section">
                    <input type="text" class="grafting-input" name="hash1" placeholder="First Grafting Component...">
                    <input type="text" class="grafting-input" name="hash2" placeholder="Second Grafting Component...">
                    <input type="text" class="grafting-input" name="hash3" placeholder="Third Grafting Component...">
                </div>

                <button type="submit" class="submit-btn">Perform Grafting Ritual</button>
            </form>
            
            <?php if ($_SERVER['REQUEST_METHOD'] === 'POST'): ?>
                <div class="message <?php echo $result['success'] ? 'success' : 'error'; ?>">
                    <?php echo htmlspecialchars($result['message']); ?>
                </div>
            <?php endif; ?>
        </div>

        <div class="hint-box">
            "In search of true vigor, I have grafted the power of champions..."
        </div>

        <!-- Hidden comment with hint -->
        <!-- The first shall speak of forefathers, the second of tarnished blood, and the last of grafted power -->
    </div>

    <!-- Challenge-related script -->
    <script>
        // Look deeper into crack_me.txt for the true path
        // MD5 hashes await in hash.txt
        // 7d1a54127b399b070140ee377ac70ea5
        // 5c29a959abce4abb8924f2c54c04b2f7
        // e99a18c428cb38d5f260853678922e03
    </script>
</body>
</html>
