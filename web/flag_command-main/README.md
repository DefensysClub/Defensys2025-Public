# ctf-challenge : flag_command
### Challenge Description:

The notorious admin of this website has left their credentials lying around, and now it's your chance to step into their shoes. But beware—this admin is no fool. They’ve hidden something valuable behind their login, and the only way to get it is to think like them.
Once you’ve gained access, you’ll need to dig deeper. The admin’s tools are powerful, but they’re not perfect. Can you exploit their oversight to uncover the hidden flag?
Hint: Sometimes, the easiest way to become someone is to carry their identity with you.

#### Hints

- Hint 1: "Sometimes, the key to unlocking the next step lies in the small, often overlooked details stored in your browser."
- Hint 2: "The treasure is locked away, but the system’s tools can be turned against it."

### Challenge Overview:

This challenge is a web exploitation task that combines session manipulation and command injection. Players must bypass authentication by forging a session cookie and then exploit a command injection vulnerability to retrieve the flag.

### Challenge Details:
- Category: Web Exploitation
- Difficulty: Easy
- Flag Format: DEFENSYS{...}
- Author: reda abdelali

### Setup Instructions:
##### Prerequisites
- Docker (optional, for containerization)
- Python 3.x
- Flask

##### Steps to Run the Challenge
- Clone the Repository
```
git clone https://github.com/RedaAbdelali/flag_command.git
  
cd flag_command
```
- Build and Run the Docker Container :
``
    docker build -t flag_command .
``
``
  docker run -p 5000:5000 flag_command
``
- Run the Flask Application Locally:
``
    python app.py
``
- Access the Challenge:

#### Challenge Walkthrough:
**Step 1: Log In**

  Use the credentials admin:admin to log in.

**Step 2: Inspect the Session Cookie**

  Use browser developer tools to inspect the session cookie.

  The session cookie is a base64 string of the session data (e.g., {"role": "user"} → eyJyb2xlIjogInVzZXIifQ==).

**Step 3: Decode the Session Cookie**

**Step 4: Forge a Session Cookie**

  Encode {"role": "admin"} as a base64 string to generate a valid session cookie.

  Replace the original session cookie with the forged one using browser developer tools.

**Step 5: Access the Admin Page**

  With the forged session cookie, navigate to the gallery page.

**Step 6: Exploit Command Injection**

  Use the file upload feature to inject a command and retrieve the flag:
``
    cat flag
``

**Step 7: Retrieve the Flag**

  The server will return the flag:

  DEFENSYS{c00k13_m4n1pul4t10n_4nd_c0mm4nd_1nj3ct10n}
