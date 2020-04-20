import static org.junit.jupiter.api.Assertions.*;



//import org.junit.Before;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.junit.jupiter.api.Test;

public class seleniumTest {

/////////////// COMBINED FILTERING AND SORTING /////////////////////////////

	
	

//PASSES	
@Test public void filterVenueByCostSortByVenueName() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Venues"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("cost")));
		we.sendKeys("$$" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.TAB,Keys.ENTER); // enter a search value
		Thread.sleep(500);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-venues")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("V" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("3rd Floor Cantina", output);
		
		wd.quit(); // close the browser window
			}
	
	
	
//PASSES
@Test public void filterConcertsByTimeSortByVenueName() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Concerts"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("time")));
		we.sendKeys("2" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.TAB,Keys.ENTER); // enter a search value
		Thread.sleep(500);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-concert")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("V" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h3"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("Elevation Worship at H-E-B Center at Cedar Park", output);
		
		wd.quit(); // close the browser window
			}
	
	

//PASSES	
@Test public void filterArtistsByPopularitySortByFollowers() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Artists"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("popularity")));
		we.sendKeys("5" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.TAB,Keys.ENTER); // enter a search value
		Thread.sleep(500);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-artists")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("F" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("Luke Combs", output);
		
		wd.quit(); // close the browser window
			}	
	
	
/////////////// SORTING /////////////////////////////


//PASSES	
@Test public void resetAfterSortConcertbyConcertName() throws InterruptedException {
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Concerts"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-concert")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("C" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));
		Thread.sleep(2000);
		we = wd.findElement(By.tagName("button"));
		we.click();
		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h3"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("The Monkees at Austin City Limits Live at The Moody Theater", output);	
		
		wd.quit(); // close the browser window
			}




//PASSES
@Test public void sortVenuebyYelpRating() throws InterruptedException {
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Venues"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-venues")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("Y" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("Vulcan Gas Company", output);	
		
		wd.quit(); // close the browser window
			}
//PASSES	
@Test public void sortConcertbyConcertName() throws InterruptedException {
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Concerts"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-concert")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("C" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h3"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("Acid Mothers Temple & The Melting Paraiso U.F.O. and Acid Mothers Temple with ST 37 at Hotel Vegas", output);	
		
		wd.quit(); // close the browser window
			}	
	
	
//PASSES	
@Test public void sortArtistbyName() throws InterruptedException {
	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	WebDriverWait wait = new WebDriverWait(wd, 100);
	we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("sort-select-artists")));
//	we = wd.findElement(By.name("popularity"));
	we.sendKeys("N" + Keys.ENTER);
	we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//	we = wd.findElement(By.id("search-btn"));
//	we.click(); //click the button
//	we = wd.findElement(By.tagName("li"));

	Thread.sleep(2000);
	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button
	
	WebElement result = wd.findElement(By.tagName("h1"));
//	System.out.println(result);
	String output = result.getText(); // read the output text
	assertEquals("Allegaeon", output);		
	
	wd.quit(); // close the browser window
		}	
	
	
/////////////// FILTERING ///////////////////////////
	
	
//PASSES	
@Test public void testResetAfterFilterVenuesByCost() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Venues"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("cost")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("$$$" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));
		
		we = wd.findElement(By.tagName("button"));
		we.click();
		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("ACL Live at The Moody Theater", output);	
		
		wd.quit(); // close the browser window
			}


//PASSES	
@Test public void filterVenuesByBoth() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Venues"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("cost")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("3" + Keys.ENTER);
		we.sendKeys(Keys.TAB);
		we.sendKeys("$"+ Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("ACL Live at The Moody Theater", output);		
		
		wd.quit(); // close the browser window
			}	
	
	
//PASSES	
@Test public void filterVenuesByCost() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Venues"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("cost")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("$$$" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("One World Theatre", output);	
		
		wd.quit(); // close the browser window
			}	
	
	
//PASSES	
@Test public void filterVenuesByRating() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Venues"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("rating")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("4" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("ACL Live at The Moody Theater", output);		//TODO: CHANGE TO CORRECT VENUE
		
		wd.quit(); // close the browser window
			}		

//PASSES
@Test public void filterConcertsByBoth() throws InterruptedException {
	
	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	WebDriverWait wait = new WebDriverWait(wd, 100);
	we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("date")));
//	we = wd.findElement(By.name("popularity"));
	we.sendKeys("0");
	Thread.sleep(500);
	we.sendKeys(Keys.ENTER);
	we = wd.findElement(By.name("time"));
	we.sendKeys("1" + Keys.ENTER);
	we.sendKeys(Keys.TAB, Keys.ENTER);


	Thread.sleep(2000);
	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button
	
	WebElement result = wd.findElement(By.tagName("h3"));
//	System.out.println(result);
	String output = result.getText(); // read the output text
	assertEquals("Whitney Rose at The Continental Club", output);		
	
	wd.quit(); // close the browser window
		}


//PASSES	
@Test public void filterConcertsByTime() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Concerts"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("time")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("2" + Keys.ENTER);
		Thread.sleep(2000);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h3"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("The Monkees at Austin City Limits Live at The Moody Theater", output);		//TODO: CHANGE TO CORRECT CONCERT
		
		wd.quit(); // close the browser window
			}		
	
	
//PASSES	
@Test public void filterConcertsByMonth() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Concerts"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("date")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("04" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h3"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("The Monkees at Austin City Limits Live at The Moody Theater", output);	
		
		wd.quit(); // close the browser window
			}	
//PASSES	
@Test public void filterArtistsByBoth() throws InterruptedException {
	
	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Artists"));
	we.click(); //click the button

	WebDriverWait wait = new WebDriverWait(wd, 100);
	we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("genre")));
//	we = wd.findElement(By.name("popularity"));
	we.sendKeys("5" + Keys.ENTER);
	we.sendKeys(Keys.TAB);
	we.sendKeys("Country" + Keys.ENTER); // enter a search value
//	we = wd.findElement(By.id("search-btn"));
//	we.click(); //click the button
//	we = wd.findElement(By.tagName("li"));

	Thread.sleep(2000);
	we = wd.findElement(By.tagName("img"));
	we.click(); //click the button
	
	WebElement result = wd.findElement(By.tagName("h1"));
//	System.out.println(result);
	String output = result.getText(); // read the output text
	assertEquals("The Monkees", output);	
	
	wd.quit(); // close the browser window
		}	

//PASSES
	@Test public void filterArtistsByGenre() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Artists"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("genre")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("C" + Keys.ENTER);
		Thread.sleep(2000);
		we.sendKeys(Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("The Monkees", output);	
		
		wd.quit(); // close the browser window
			}	
	
//PASSES	

	@Test public void filterArtistsByPopularity() throws InterruptedException {
		
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.linkText("Artists"));
		we.click(); //click the button

		WebDriverWait wait = new WebDriverWait(wd, 100);
		we = wait.until(ExpectedConditions.presenceOfElementLocated(By.name("popularity")));
//		we = wd.findElement(By.name("popularity"));
		we.sendKeys("8" + Keys.ENTER);
		we.sendKeys(Keys.TAB,Keys.TAB,Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
//		we = wd.findElement(By.tagName("li"));

		Thread.sleep(2000);
		we = wd.findElement(By.tagName("img"));
		we.click(); //click the button
		
		WebElement result = wd.findElement(By.tagName("h1"));
//		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("Luke Combs", output);
		
		wd.quit(); // close the browser window
			}
		
//////////// SEARCHING ////////////////////////////
//PASSES
	@Test public void searchAustinInArtists() {	
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.tagName("select"));
		we.sendKeys("A" + Keys.ENTER);
		we = wd.findElement(By.id("search-txt"));
		we.sendKeys("austin" + Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
		WebDriverWait wait = new WebDriverWait(wd, 100);
		WebElement result;
		result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("p")));
		
		//result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
		//WebElement result; = wd.findElement(By.tagName("h4"));
		
		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("8 results", output);
		wd.quit(); // close the browser window
			}	
	
	
	
	
//PASSES	
@Test public void searchBarracudaInConcerts() {	
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.tagName("select"));
		we.sendKeys("C" + Keys.ENTER);
		we = wd.findElement(By.id("search-txt"));
		we.sendKeys("barracuda" + Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
		WebDriverWait wait = new WebDriverWait(wd, 100);
		WebElement result;
		result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("p")));
		
		//result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
		//WebElement result; = wd.findElement(By.tagName("h4"));
		
		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("10 results", output);
		wd.quit(); // close the browser window
			}


	
//PASSES
@Test public void noResults() {	
		System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
		WebDriver wd = new FirefoxDriver(); // launch the browser
		wd.get("http://127.0.0.1:8000");
		WebElement we = wd.findElement(By.id("search-txt"));
		we.sendKeys("hello" + Keys.ENTER); // enter a search value
//		we = wd.findElement(By.id("search-btn"));
//		we.click(); //click the button
		WebDriverWait wait = new WebDriverWait(wd, 100);
		WebElement result;
		result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("p")));
		
		//result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
		//WebElement result; = wd.findElement(By.tagName("h4"));
		
		System.out.println(result);
		String output = result.getText(); // read the output text
		assertEquals("0 results", output);
		wd.quit(); // close the browser window
			}	


// PASSES	
@Test public void searchEDENInAll() {	
	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.id("search-txt"));
	we.sendKeys("eden" + Keys.ENTER); // enter a search value
//	we = wd.findElement(By.id("search-btn"));
//	we.click(); //click the button
	WebDriverWait wait = new WebDriverWait(wd, 100);
	WebElement result;
	result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
	
	//result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
	//WebElement result; = wd.findElement(By.tagName("h4"));
	
	System.out.println(result);
	String output = result.getText(); // read the output text
	assertEquals("Showing Search Results for: \"eden\" in All", output);
	wd.quit(); // close the browser window
		}

//PASSES
@Test public void searchBarracudaInVenues() {	
	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.tagName("select"));
	we.sendKeys("V" + Keys.ENTER);
	we = wd.findElement(By.id("search-txt"));
	we.sendKeys("barracuda" + Keys.ENTER); // enter a search value
//	we = wd.findElement(By.id("search-btn"));
//	we.click(); //click the button
	WebDriverWait wait = new WebDriverWait(wd, 100);
	WebElement result;
	result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
	
	//result = wait.until(ExpectedConditions.presenceOfElementLocated(By.tagName("h4")));
	//WebElement result; = wd.findElement(By.tagName("h4"));
	
	System.out.println(result);
	String output = result.getText(); // read the output text
	assertEquals("Showing Search Results for: \"barracuda\" in Venues", output);
	wd.quit(); // close the browser window
		}	


///////////////////////////////////////////////////////////////////////////////////////////


	



//PASSES
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

//PASSES
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

//PASSES
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
	assertEquals("The Monkees", output);
	wd.quit(); // close the browser window
	}

//PASSES
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
	assertEquals("Face To Face", output);
	wd.quit(); // close the browser window
	}

//PASSES
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

//PASSES
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



//PASSES
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
	assertEquals("Hotel Vegas", output);	
	wd.quit(); // close the browser window
	}


//PASSES
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


//PASSES
@Test public void clickOneConcert() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");

	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("li"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h3"));
	String output = result.getText(); // read the output text
	assertEquals("The Monkees at Austin City Limits Live at The Moody Theater", output);	
	wd.quit(); // close the browser window
	}

//PASSES
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

	WebElement result = wd.findElement(By.tagName("h3"));
	String output = result.getText(); // read the output text
	assertEquals("Face To Face with Sharp Shock at Empire Control Room & Garage", output);	
	wd.quit(); // close the browser window
	}


//PASSES
@Test public void clickOneConcertOnLastPage() {

	System.setProperty("webdriver.gecko.driver","/Users/dylanwolford/Downloads/geckodriver");
	WebDriver wd = new FirefoxDriver(); // launch the browser
	//wd.get("http://www.austindatabass.appspot.com");
	wd.get("http://127.0.0.1:8000");	
	WebElement we = wd.findElement(By.linkText("Concerts"));
	we.click(); //click the button

	we = wd.findElement(By.linkText("last »"));
	we.click(); //click the button

	we = wd.findElement(By.tagName("li"));
	we.click(); //click the button

	WebElement result = wd.findElement(By.tagName("h3"));
	String output = result.getText(); // read the output text
	assertEquals("All Good Things at Come and Take It Live", output);	
	wd.quit(); // close the browser window
	}
	
}

