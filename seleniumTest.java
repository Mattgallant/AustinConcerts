import static org.junit.jupiter.api.Assertions.*;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;


import org.junit.jupiter.api.Test;

public class phase2Test {

@Before 
public void setproperties(){
	System.setProperty("webdriver.gecko.driver","/AustinConcerts/geckodriver");	
}


@Test public void clickAustinDataBass() {

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

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Artists", output);
	wd.quit(); // close the browser window
	}

@Test public void clickOneArtist() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("Josh Kelley"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
	String output = result.getText(); // read the output text
	assertEquals("Austin Data Bass - Josh Kelley", output);
	wd.quit(); // close the browser window
	}

@Test public void clickOneArtistOnPage2() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("next"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("PEARS"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
	String output = result.getText(); // read the output text
	assertEquals("Austin Data Bass - PEARS", output);
	wd.quit(); // close the browser window
	}


@Test public void clickVenues() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Venues"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("h1"));
	String output = result.getText(); // read the output text
	assertEquals("Venues", output);	
	wd.quit(); // close the browser window
	}

@Test public void clickOneVenue() {

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



@Test public void clickOneVenueOnPage2() {

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


@Test public void clickConcerts() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
	String output = result.getText(); // read the output text
	assertEquals("Austin Data Bass - Concerts", output);	
	wd.quit(); // close the browser window
	}

@Test public void clickOneConcert() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("Elle Limebear at H-E-B Center at Cedar Park"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
	String output = result.getText(); // read the output text
	assertEquals("Austin Data Bass - Elle Limebear at H-E-B Center at Cedar Park", output);	
	wd.quit(); // close the browser window
	}

@Test public void clickOneConcertOnPage2() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("next"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("Math Judson at Sahara Lounge"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
	String output = result.getText(); // read the output text
	assertEquals("Austin Data Bass - Math Judson at Sahara Lounge", output);	
	wd.quit(); // close the browser window
	}


@Test public void clickOneConcertOnLastPage() {

	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://www.austindatabass.appspot.com");
	we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("last »"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("Josh Kelley with Harper Grae at Mohawk"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.find_element_by_tag_name("title"));
	String output = result.getText(); // read the output text
	assertEquals("Austin Data Bass - Josh Kelley with Harper Grae at Mohawk", output);	
	wd.quit(); // close the browser window
	}
