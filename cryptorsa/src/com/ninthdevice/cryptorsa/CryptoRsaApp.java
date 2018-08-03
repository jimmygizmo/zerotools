package com.ninthdevice.cryptorsa;

import java.security.*;
import java.io.*;
import java.security.spec.*;
import javax.crypto.Cipher;

// For reading file into byte array
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;

public class CryptoRsaApp {

    private static PublicKey loadPublicKey(String filename) throws IOException, NoSuchAlgorithmException, InvalidKeySpecException {
        File file = new File(filename);
        int fileLength = (int)file.length();
        DataInputStream dataInputStream = new DataInputStream(new FileInputStream(file));
        byte[] keyBytes = new byte[fileLength];
        dataInputStream.readFully(keyBytes);
        dataInputStream.close();

        X509EncodedKeySpec spec = new X509EncodedKeySpec(keyBytes);
        KeyFactory kf = KeyFactory.getInstance("RSA");
        return kf.generatePublic(spec);
    }

    private static byte[] encryptBytes(byte[] bs, PublicKey key) throws NoSuchAlgorithmException, GeneralSecurityException {
        byte[] cipherText = null;
        final Cipher cipher = Cipher.getInstance("RSA/ECB/NOPADDING");
        cipher.init(Cipher.ENCRYPT_MODE, key);
        cipherText = cipher.doFinal(bs);
        return cipherText;
    }

    public static void main(String[] args) throws Exception {
        PublicKey publicKey = loadPublicKey("/Users/bilbo/GITREPOS/zerotools/cryptorsa/public_key.der");

        // NOTE: To load text file into bytearray could use:
        // IOUtils.toByteArray(InputStream input) in Apache Commons

        Path inFilePath = Paths.get("/Users/bilbo/GITREPOS/zerotools/cryptorsa/plaintext.txt");
        byte[] plainTextBytes = Files.readAllBytes(inFilePath);

        byte[] cipherTextBytes = encryptBytes(plainTextBytes, publicKey);

        Path outFilePath = Paths.get("/Users/bilbo/GITREPOS/zerotools/cryptorsa/cipher_text.dat");

        Path fileBytesWrittenTo = Files.write(outFilePath, cipherTextBytes);

        System.out.println("Ciphertext bytes written to: " + fileBytesWrittenTo.toString());

    }
}

