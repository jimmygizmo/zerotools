package com.ninthdevice.helloworld;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


/**
 * Test in browser at http://localhost:8080/hello?name=Wooorrrld
 *
 * Current Maven build config works to run this standalone specifying classpath like this:
 * java -cp ./helloworld.jar com.ninthdevice.helloworld.HelloWorldApplication
 * BUT not like this:
 * java -jar ./helloworld.jar
 * TODO: So our jar is not yet an executable jar.
 *
 * */
@SpringBootApplication
public class HelloWorldApplication {

    public static void main(String[] args) {
        SpringApplication.run(HelloWorldApplication.class, args);
    }
}
