import static org.junit.jupiter.api.Assertions.*;

import org.junit.Before;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;


import org.junit.jupiter.api.Test;

public class seleniumTest {


@Test public void clickAbout() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("About"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("About Us", output);
	wd.quit(); // close the browser window
	}

@Test public void clickArtists() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Artists", output);
	wd.quit(); // close the browser window
	}


@Test public void clickOneArtist() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("li"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Dale Watson", output);
	wd.quit(); // close the browser window
	}

@Test public void clickOneArtistOnPage2() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	we = wd.findElement(By.partialLinkText("next"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("li"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Ted Hajna", output);
	wd.quit(); // close the browser window
	}

*/

@Test public void clickVenues() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Venues"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Venues", output);	
	wd.quit(); // close the browser window
	}

@Test public void clickOneVenue() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Venues"));	we.click(); //click the button

	we = wd.findElement(By.tagName("li"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("ACL Live at The Moody Theater", output);	
	wd.quit(); // close the browser window
	}



@Test public void clickOneVenueOnPage2() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Venues"));	we.click(); //click the button

	we = wd.findElement(By.linkText("next"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Spider House", output);	
	wd.quit(); // close the browser window
	}
/*

@Test public void clickConcerts() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Concerts", output);	
	wd.quit(); // close the browser window
	}



@Test public void clickOneConcert() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Elle Limebear at H-E-B Center at Cedar Park", output);	
	wd.quit(); // close the browser window
	}

@Test public void clickOneConcertOnPage2() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");	
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("next"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Math Judson at Sahara Lounge", output);	
	wd.quit(); // close the browser window
	}


@Test public void clickOneConcertOnLastPage() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");	
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("last »"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Josh Kelley with Harper Grae at Mohawk", output);	
	wd.quit(); // close the browser window
	}
	*/
}

