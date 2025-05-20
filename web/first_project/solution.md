In the CTF description, the author mentioned that this is their first project and that they used Python templates and made them dynamic, which likely means there is an SSTI vulnerability.

So, we need to identify which input allows us to insert code for exploitation.

After reading the app.py code, I noticed that all inputs are only stored in the users.txt file, except for the Name field entered when creating a new account, as it is printed later. So, we can test by entering {{7 * 7}}, and if 49 is printed, it confirms that this input is vulnerable to SSTI and can be exploited.

[![image.png](hhttps://i.postimg.cc/KYTWc6bR/1.png)](https://postimg.cc/4KJPBFmg)
[![image.png](https://i.postimg.cc/j2x3XC77/2.png)](https://postimg.cc/47014fwf)

Since the test was successful, we can exploit this input. After reading the app.py code, I noticed that all user information is stored in users.txt, but the username and password are saved as hashes. I also observed that the flag structure appears when logging in as admin, and that the admin’s information is also stored in users.txt. So, if we can read users.txt, we can deduce the admin's credentials and obtain the flag.

I will enter the following command in the Name input field to view user data, including admin :

```shell
{{ cycler.__init__.__globals__.os.popen('cat users.txt').read() }}
```

[![image.png](https://i.postimg.cc/bYgBv07H/3.png)](https://postimg.cc/py9ZGjXp)
[![image.png](https://i.postimg.cc/Qd26zf7s/4.png)](https://postimg.cc/75NMGMXQ)

As we can see, the command worked, but there are many users, and we don’t know which one is admin. Moreover, even if we identify admin, we cannot retrieve the username and password because they are stored as hashes.

When going back to the Create an Account page, I noticed that admin provided examples of how the username is generated. It is created using only the first name (Name), last name (Last Name), and age (Age).

Additionally, he left a comment stating that the password is the most important part and should not contain personal information, while having personal details in the username is not an issue.

For example, if the name is John, the last name is Doe, and the age is 25, then the username would be: johndoe25.

[![image.png](https://i.postimg.cc/bv16f10n/5.png)](https://postimg.cc/McK0yMFZ)

So, it is likely that the admin's username was created using this structure. This means that if we know the first name, the last name, and the age of the admin, we can figure out the username. To find the admin's first name, last name, and age, we will search through all the users and identify the one who followed this pattern when creating their username. Since few users follow these examples, but admin provided them, it is likely that admin followed the same method.

So, we will make a copy of those users into the txt.txt file and then search for the pattern using shell commands.

```shell
grep -oP "[A-Z][a-z A-Z]+:[A-Z][a-z A-Z]+:[0-9]+:[A-Z][a-z A-Z]+:[A-Z][a-z A-Z]+:[A-Z][a-z A-Z]+:[A-Z][a-z A-Z]+:[a-f0-9]{64}:[a-f0-9]{64}" txt.txt |  awk -F: '{
    # Convert first and last name to lowercase and concatenate with age
    cmd = "echo -n \"" tolower($1) tolower($2) $3 "\" | sha256sum"     
    
    # Compute SHA-256 hash
    cmd | getline hash    
    close(cmd)
    
    # Compare the computed hash with the stored hash in field 8
    if (hash ~ $8) print $0
}'
```

[![image.png](https://i.postimg.cc/0QfcbxB2/6.png)](https://postimg.cc/FdYj6tv2)
[![image.png](https://i.postimg.cc/mkgV9qv3/7.png)](https://postimg.cc/MMgy2sKX)

As expected, only two users followed the structure, so most likely one of them is the admin, but how can we be sure?

If we carefully read the code in app.py, we notice in the check_credentials function that only if the username and password are recognized in the users.txt file, it returns true. In both cases, whether the user is normal or admin, it returns true. Then, on the /dashboard page, it distinguishes between showing the structure flag or just displaying "good job" based only on the username. If the username belongs to the admin but the code is not specifically for the admin, yet it is registered in users.txt, the structure flag will also be shown. Therefore, we will create two accounts using the same method of combining name + last_name + age in username, and then log in. The account that gives us the structure flag is the admin account.

[![image.png](https://i.postimg.cc/2j00YkW0/8.png)](https://postimg.cc/kDtQFdfS)
[![image.png](https://i.postimg.cc/9FzJF6tC/9.png)](https://postimg.cc/6yJdM1mm)
[![image.png](https://i.postimg.cc/qMYQt1jn/10.png)](https://postimg.cc/Mv71NmkK)
[![image.png](https://i.postimg.cc/BnKp22Vz/11.png)](https://postimg.cc/K1mt23F7)

So, the process was successful, and the second account is the admin account.

So, the flag is :

DEFENSYS{Jones_22_Philadelphia_Gaming_CyberM48}