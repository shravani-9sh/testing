import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class Testing {
    @Test
    public void ChromeTest(){

        System.out.println("The thread ID for Chrome is "+ Thread.currentThread().getId());
        System.setProperty("webdriver.chrome.driver","/Users/shravani/Documents/codebase/AutomarionProject/driver/chromedriver" );
        WebDriver driver = new ChromeDriver();
        driver.get("https://www.facebook.com");
        driver.quit();
    }
}



