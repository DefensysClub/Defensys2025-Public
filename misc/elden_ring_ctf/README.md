# Elden Ring CTF Challenges

## **1. Malenia's Challenge**
**Level**: Beginner  
**Category**: Web, OSINT  

### **Description**
Malenia, Blade of Miquella, guards the first part of the flag. To defeat her, players must inspect her domain carefully and uncover hidden secrets.

### **Objectives**
Players must:
1. Inspect the browser console to find the first clue.
2. Discover the hidden `secret_code.txt` file.
3. Decode a Base64-encoded password.
4. Submit the correct password in the form to defeat Malenia.

### **Hints**
- The web console (`F12 > Console`) may hold useful information.
- Base64 decoding tools are available online or via CLI (`echo "BASE64_STRING" | base64 -d`).
- The secret lies in `/kingdom_malenia/`.

### **Solution Walkthrough**
1. Inspect **`vulnerability.js`** via Developer Tools (Console).
2. Find a reference to `/kingdom_malenia/secret_code.txt`.
3. Navigate to `http://localhost:8080/kingdom_malenia/secret_code.txt` to find the encoded password.
4. Decode it using Base64 to get **`Malenia_secret`**.
5. Enter **`Malenia_secret`** into the form on `boss.php`.
6. If correct, Malenia is defeated, and the player receives a hint for Radahn.

---

## **2. Radahn's Challenge**
**Level**: Intermediate  
**Category**: Web, Steganography  

### **Description**
Radahn, Starscourge, has hidden his secrets deep within the stars. To unlock his knowledge, players must extract hidden information from an image.

### **Objectives**
Players must:
1. Download the `radahn.jpg` image from `battle.php`.
2. Use steganography tools to extract hidden data.
3. Submit the correct hidden message in the form.
4. Receive a hint for the next challenge.

### **Hints**
- Steganography is the art of hiding data in images.
- Use an online tool like [Steganography Tool](https://stylesuxx.github.io/steganography/) or a CLI tool (`steghide`).
- If using `steghide`, try:
  ```bash
  steghide extract -sf radahn.jpg
  
  ### **Solution Walkthrough**

1. Download `radahn.jpg` from `http://localhost:8080/kingdom_radahn/battle.php`.
2. Use [Steganography Tool](https://stylesuxx.github.io/steganography/) to extract the hidden text.
3. The extracted message is **`Starscourge_Radahn`**.
4. Enter **`Starscourge_Radahn`** into the form.
5. If correct, Radahn is defeated, and the player receives a hint for Godrick.


## Godrick's Challenge
Level: Intermediate
Category: Web, Cryptography

Players must:
1. Crack three MD5 hashes
2. Decode a multi-part encoded message
3. Submit the components in correct order
4. Combine all parts to get the final flag


Flag: `defensys{Malenia_secretStarscourge_RadahnG0DR1CK_TH3_GR4FT3D}`