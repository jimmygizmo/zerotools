#! /bin/bash

echo
echo "Generating rsa 1024 bit private key in file private.pem"
echo "EXECUTING: openssl genrsa -out private.pem 1024"
echo

openssl genrsa -out private.pem 1024

sleep 4s

echo
echo "Examination of this private.pem key file gives the following information:"
echo "EXECUTING: openssl rsa -in private.pem -noout -text"
echo

sleep 4s

openssl rsa -in private.pem -noout -text

echo
echo "* The modulous IS the public key."
echo "* The privateExponent IS the private key."
echo "Now this private key can be used to generate a public key in another format if desired."
echo

##
#

