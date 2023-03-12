import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.annotations.Test;

import java.time.Duration;

public class Base {

        @Test
        public void reCaptchaTest() throws InterruptedException {

            System.out.println("The thread ID for Chrome is " + Thread.currentThread().getId());
            System.setProperty("webdriver.chrome.driver", "/Users/shravani/Documents/codebase/AutomarionProject/driver/chromedriver");
            ChromeDriver driver = new ChromeDriver();
            driver.get("https://pdmpqanew.logicoy.com/cas/login?service=https%3A%2F%2Fpdmpqanew.logicoy.com%2FPDMPSystemApp%2Flogin%2Fcas");
            driver.findElement(By.xpath("//input[@id='username']")).sendKeys("shravani95n@gmail.com");
            driver.findElement(By.xpath("//input[@id='password']")).sendKeys("Test@1234");
            Thread.sleep(3000);
            driver.findElement(By.xpath("//div[@class='recaptcha-checkbox-border']")).click();
            Thread.sleep(3000);
            driver.findElement(By.xpath("//button[@id='recaptcha-audio-button']")).click();
            Thread.sleep(3000);
            driver.findElement(By.xpath("(//button[@class='rc-button-default goog-inline-block'])[1]")).click();
            driver.quit();
        }

    }

