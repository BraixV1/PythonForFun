package Java.Java_009.numbers;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.Properties;

public class NumberConverter {

    public static void main(String[] args) {
        NumberConverter converter = new NumberConverter("en");
        System.out.println(converter.numberInWords(100));
    }


    public NumberConverter(String lang) {
        this.prop = readProperties(lang);
        if(this.prop.size() < 1) {
            throw new MissingTranslationException(lang);
        }

    }

    private Properties prop;

    public Properties readProperties(String lang) {
        String filePath = "src/exceptions/numbers/numbers_" + lang + ".properties";
        
        Properties properties = new Properties();
        FileInputStream is = null;

        try {
            is = new FileInputStream(filePath);

            InputStreamReader reader = new InputStreamReader(
                    is, StandardCharsets.UTF_8);

            properties.load(reader);
        } catch (FileNotFoundException e) {
            // handle exceptions
            throw new MissingLanguageFileException(lang, e);
        } catch (Exception e) {
            throw new BrokenLanguageFileException(lang,e);
        } finally {
            close(is);
        }
        return properties;
    }


    private static void close(FileInputStream is) {
        if (is == null) {
            return;
        }

        try {
            is.close();
        } catch (IOException ignore) {}
    }

    public static int division(int num) {
        String result = "1";
        for (int i = num-1; i > 0; i--) {
            result += '0';
        }
        return Integer.parseInt(result);
    }

    private String hundreds(int number, boolean isalone){
        String result;

        if(isalone) {
            result = this.prop.getProperty(String.valueOf(number/division(3)))
            + this.prop.getProperty("hundreds-before-delimiter")
            + this.prop.getProperty("hundred");
            return result;
        } else {
            result = this.prop.getProperty(String.valueOf(number/division(3)))
            + this.prop.getProperty("hundreds-before-delimiter")
            + this.prop.getProperty("hundred")
            + this.prop.getProperty("hundreds-after-delimiter");
            return result;
        }
    }

    private String tens(int number, boolean isalone) {
        String result = "";
    
        if (number > 19) {
            int tempNumber = number / 10 * 10;
            if (isalone && this.prop.containsKey(String.valueOf(tempNumber))) {
                result += this.prop.getProperty(String.valueOf(tempNumber));
                return result;
            } else if (!isalone && this.prop.containsKey(String.valueOf(tempNumber))) {
                result += this.prop.getProperty(String.valueOf(tempNumber)) + this.prop.getProperty("tens-after-delimiter");
                return result;
            }
        }
    
        if (isalone && this.prop.containsKey(String.valueOf(number))) {
            result += this.prop.getProperty(String.valueOf(number));
            return result;
        } else if (!isalone && this.prop.containsKey(String.valueOf(number))) {
            result += this.prop.getProperty(String.valueOf(number)) + this.prop.getProperty("tens-after-delimiter");
            return result;
        } else if (!this.prop.containsKey(String.valueOf(number)) && number < 20) {
            result = this.prop.getProperty(String.valueOf(number % 10)) + prop.getProperty("teen");
            return result;
        } else if (!isalone && !this.prop.containsKey(String.valueOf(number)) && number >= 20) {
            result = this.prop.getProperty(String.valueOf(number / 10)) + this.prop.getProperty("tens-suffix") + this.prop.getProperty("tens-after-delimiter");
            return result;
        } else if (isalone && !this.prop.containsKey(String.valueOf(number)) && number >= 20) {
            result = this.prop.getProperty(String.valueOf(number / 10)) + this.prop.getProperty("tens-suffix");
            return result;
        }
        return result;
    }
    
    private String ones(int number){
        return this.prop.getProperty(String.valueOf(number));
    }

    private String checkTens(int remainder){
        String result = "";
        if(remainder > 19){
            if(remainder % division(2) > 0){
                result += tens(remainder, false);
            } else {
                result += tens(remainder, true);
                return result;
            }// check if result is not null
            remainder = remainder % division(2);
            result += ones(remainder);
            return result;
        } else {
            result += tens(remainder, true);
            return result;
        }
    }
    


    public String numberInWords(Integer number) {
        String result = "";
        int remainder;
        if(String.valueOf(number).length() == 3){
            remainder = number % division(3);
            if(remainder > 0){
                result += hundreds(number, false);
            } else {
                result += hundreds(number, true);
                return result;
            }
            result += checkTens(remainder);
            return result;
        }
        if(String.valueOf(number).length() == 2) {
            result += checkTens(number);
            return result;
        } else {
            result += ones(number);
            return result;
        }
        
    }
}

