package com.wolf.selfservicecourierweb.Tools;

import com.wolf.selfservicecourierweb.Entity.Goods;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SendSmsTool {

    public static String send(Goods goods) {

        String username = "user"; //在短信宝注册的用户名
        String password = "password"; //在短信宝注册的密码
        String template = "【科院快递中心】您的快递单号 %s 已到达校快递中心（校图书馆对面），货柜号 %s ，取件码 %s 为了您快件的安全，请不要把提货码泄露给其他人。";
        String testContent = String.format(template, goods.getExpressNumber(), goods.getContainerNumber(), goods.getPickUpCode());

        String httpUrl = "http://api.smsbao.com/sms";

        StringBuffer httpArg = new StringBuffer();
        httpArg.append("u=").append(username).append("&");
        httpArg.append("p=").append(md5(password)).append("&");
        httpArg.append("m=").append(goods.getPhone()).append("&");
        httpArg.append("c=").append(encodeUrlString(testContent, "UTF-8"));

        String result = request(httpUrl, httpArg.toString());
        return result;
    }

    public static String request(String httpUrl, String httpArg) {
        BufferedReader reader = null;
        String result = null;
        StringBuffer sbf = new StringBuffer();
        httpUrl = httpUrl + "?" + httpArg;

        try {
            URL url = new URL(httpUrl);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();
            InputStream is = connection.getInputStream();
            reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            String strRead = reader.readLine();
            if (strRead != null) {
                sbf.append(strRead);
                while ((strRead = reader.readLine()) != null) {
                    sbf.append("\n");
                    sbf.append(strRead);
                }
            }
            reader.close();
            result = sbf.toString();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }

    public static String md5(String plainText) {
        StringBuffer buf = null;
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(plainText.getBytes());
            byte b[] = md.digest();
            int i;
            buf = new StringBuffer("");
            for (int offset = 0; offset < b.length; offset++) {
                i = b[offset];
                if (i < 0)
                    i += 256;
                if (i < 16)
                    buf.append("0");
                buf.append(Integer.toHexString(i));
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return buf.toString();
    }

    public static String encodeUrlString(String str, String charset) {
        String strret = null;
        if (str == null)
            return str;
        try {
            strret = java.net.URLEncoder.encode(str, charset);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
        return strret;
    }
}
