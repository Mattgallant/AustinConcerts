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
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Austin Data Bass"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass", output);
wd.quit(); // close the browser window
	}


@Test public void clickAbout() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("About"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("About", output);
wd.quit(); // close the browser window
	}

@Test public void clickArtists() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Artists"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("h1"));
String output = result.getText(); // read the output text
assertEquals("Artists", output);
wd.quit(); // close the browser window
	}

@Test public void clickConcerts() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Concerts"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("h1"));
String output = result.getText(); // read the output text
assertEquals("Concerts", output);	//TODO: should this be upcoming concerts????? 
wd.quit(); // close the browser window
	}

@Test public void clickVenues() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Venues"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("h1"));
String output = result.getText(); // read the output text
assertEquals("Venues", output);	//TODO: should this be upcoming concerts????? 
wd.quit(); // close the browser window
	}

