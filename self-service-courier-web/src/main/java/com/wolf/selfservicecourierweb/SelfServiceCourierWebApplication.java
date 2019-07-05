package com.wolf.selfservicecourierweb;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication()
@MapperScan("com.wolf.selfservicecourierweb.Mapper")
public class SelfServiceCourierWebApplication {

    public static void main(String[] args) {
        SpringApplication.run(SelfServiceCourierWebApplication.class, args);
    }

}
