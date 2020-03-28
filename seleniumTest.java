import static org.junit.jupiter.api.Assertions.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;


import org.junit.jupiter.api.Test;

public class MinWebTest {
@Test public void clickAustinDataBass() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
// edit the next line to enter the location of "min.html" on your file system
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Austin Data Bass"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass", output);
wd.quit(); // close the browser window
	}


@Test public void clickAbout() {
System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
// edit the next line to enter the location of "min.html" on your file system
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("About"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("About", output);
wd.quit(); // close the browser window
	}

