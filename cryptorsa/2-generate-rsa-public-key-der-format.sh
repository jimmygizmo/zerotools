#! /bin/bash

echo
echo "Generating rsa der format public key from private key in file private.pem"
echo "Public key will be output in the file public_key.der"
echo "EXECUTING: openssl rsa -in ./private.pem -pubout -outform DER -out public_key.der"
echo

sleep 4s

openssl rsa -in ./private.pem -pubout -outform DER -out public_key.der

echo
echo "This der format public key in file public_key.der is appropriate to import into Java."
echo

##
#

