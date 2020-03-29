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
assertEquals("Austin Data Bass - About", output);
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

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass - Concerts", output);	
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
assertEquals("Venues", output);	
wd.quit(); // close the browser window
	}

@Test public void clickOneArtist() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Artists"));
we.click(); //click the button

we = wd.findElement(By.linkText("Kesha"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass - Kesha", output);
wd.quit(); // close the browser window
	}

@Test public void clickOneVenue() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Venues"));
we.click(); //click the button

we = wd.findElement(By.linkText("ACL Live at The Moody Theater"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass - ACL Live at The Moody Theater", output);	
wd.quit(); // close the browser window
	}

@Test public void clickOneArtistOnPage2() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Artists"));
we.click(); //click the button

we = wd.findElement(By.linkText("next"));
we.click(); //click the button

we = wd.findElement(By.linkText("Metallica"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass - Metallica", output);
wd.quit(); // close the browser window
	}

@Test public void clickOneVenueOnPage2() {
System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");
WebDriver wd = new FirefoxDriver(); // launch the browser
wd.get("http://www.austindatabass.appspot.com");
we = wd.findElement(By.linkText("Venues"));
we.click(); //click the button

we = wd.findElement(By.linkText("next"));
we.click(); //click the button

we = wd.findElement(By.linkText("Continental Club"));
we.click(); //click the button

WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
String output = result.getText(); // read the output text
assertEquals("Austin Data Bass - Continental Club", output);	
wd.quit(); // close the browser window
	}

