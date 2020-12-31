![alt text](static/images/Homescreen.png)
Marketsquare is an online market place designed to bridge the gap between buyers and 
sellers by providing a website where individuals, retail, and wholesale stores can 
advertise their products. Marketsquare provides the convenience of searching products
or items by visitors of the website looking to make a purchase, connecting them directly 
to the seller. Marketsquare was designed by Segun Ayodele as the third milestone project
on the Diploma in Software Development at Code Institute.

## UX
### Users Goal
* Helps sellers and buyers transact remotely.
* Gives buyers access to variety of products and multiple vendors to compare
* Eliminates the barrier of closing time as Marketsquare runs continously without closing.
* Provides sellers with the ability to list as many product as they want and also manage 
    and update their listings.

### Business Goal
* To create a platform that connects buyers and sellers together.
* To grow a database of vendors and on a global scale for marketing and reseach purposes.
* To provide ease of transaction for buyers and vendors without the limitation of time and distance.

### User Story
#### Persona
Anna is a software developer that just secured a job outside the country, she has 
some household items and furnitures she wants to sell before relocating.
Justin is a craftsman that specializes in woodwork and he is looking for means of selling his 
works without renting an outlet to showcase his craft.
They both:
* Register on Marketsquare and created a profile.
* Listed the items they want to sell with detailed Information.
* Manage information of listed items and delete items that are out of stock.

Tina's friend needs a laptop for studies, her friend cannot afford it at the moment 
so Tina has decided to buy a used laptop for her friend,so;
* Tina visits Marketsquare and searched for a laptop in the search engine.
* Tina gets a search result of laptops listed on Marketsquare.
* Tina clicks on the ones with competitive prices to read more about them.
* Tina decides to go with the last viewed laptop and gets the contact of the vendor.
* Tina negotiates with the vendor and carry out the transaction.



### Design Choice

**Fonts**
* Open Sans
* Bellota
* Pacifico

**Colour**
![alt text](static/images/Color_scheme.png)

**WireFrame**
* Mobile view
![alt text](static/images/Home_page_Wire-20.jpg)
* Desktop view
![alt text](static/images/Mobile_view-20.jpg)




## Features
### Existing Features
* __Navbar__ features on every page of the website and contains the brand name links to homepage, menu-links to register 
    and login pages and also navigation around the website.
![alt text](static/images/Navbar.png)
* __Footer__ features on all the pages and also contains navigation links around the website, social media icons, 
    category buttons and links to register and login pages.
![alt text](static/images/footer.png)
* __Home page__ contains the landing image where the welcome message and also the search engine for visitors 
    to search for items they want to buy.
    Next on the home page is the category section which features the buttons of existing categories that buyers 
    can use to filter the items displaying to a specific category.
    Also featured on the home page is the listed items section where products and items listed for scale
    is displayed before a search is carried out.
![alt text](static/images/Homescreen1.png)
    Next to the listed items section is How it works section explaining in three steps how the website works
* __User profile page__ contains the information and profile picture of a registered vendor with an update 
    button that allows the vendor to update personal information, also on the page is the items listed by 
    the vendor which also gives the vendor the ability to update or delete a listed item. a vendor will only 
    access this page on registering or login.
![alt text](static/images/Profile_page.png)
* __Item Listing page__ can only be accessed by logged in users and this is where new items or products are 
    uploaded into the database and every item is connected to the vendor through a unique id.
![alt text](static/images/Item_listing.png)
* __Register page__ is where a new user creates an acount with some information required of the user,such as 
    username, email, password, phone, and city which are recieved through a simple input form.
![alt text](static/images/register_page.png)
* __Login page__ provides a standard login form for registered user to access their personal profile and 
    listings. The login form requests an email and password for a user to sign in.
![alt text](static/images/login_page.png)
* __Log out__ allows a signed in user to log out of their page therefore clearing their user session and 
    redirecting to the login page.



## Technology Used

### Tools
* __Adobe Illustrator__ used for wireframe design.
* __Adobe Photoshop__ used for image resize and compression.
* __Git__ for version control
* __Heroku__ for hosting of the website.
* __Coolors.co__ for color palette generation.


### Libraries
* [Bootstrap](https://getbootstrap.com/) To simplify the responsiveness and the structure of the website.
* [Google Fonts](https://fonts.google.com/) for font styling.
* [jQuery](https://jquery.com/) To simplify DOM manipulation.
* [Font Awasome](https://fontawesome.com/) To incorporate icons.
* [Jinja Framework](https://jinja.palletsprojects.com/en/2.11.x/) Used for template execution and code re-usability.

### Programming Languages
* HTML
* CSS 
* Javascript
* Python

### Database
* MongoDB


## Test
The following tools were used to validate and beautify the codes:
* [Freeformatter](https://www.freeformatter.com/html-formatter.html#ad-output) used to beautify the HTML code.
* [BeautyTools](http://beautifytools.com/css-validator.php) used to beautify and validate the Javascript and CSS codes.

The navigation and buttons on this website has been tested, navigations all links to indended pages and the buttons 
functions as expected.
The authentication requires an email and password to login, giving access to more functionalities and pages such as user profile,
update profile, list items, update and deleting of items listed by same user.
This website database is mongoDB and all the endpoints created to carry out CRUD operations works properly; registered 
users of this website can create, read, update and delete data in the database.

### Limitations
* Marketsquare does not have location feature therefore can not connect buyer and seller based on proximity.
* Marketsquare requires authentication for only buyers therefore there is no chat functionality between a buyer and seller.
* There is no shopping cart functionality currently on Marketsquare website.


## Deployment
Hope Diagnostics is deployed and hosted on github pages.
At the setup stage of this project, it was connected to Heroku such that every Git push automatically updates on Heroku.
Files required by Heroku such as Procfile and requirements.txt have been added.


## Credits
### Media
* The photos used for this project (with the exception images uploaded by user) were obtained from:
    * [Pexels](https://www.pexels.com/)
Credits:
Photo by Ketut Subiyanto from Pexels
Photo by Andrea Piacquadio from Pexels
Photo by energepic.com from Pexels
Photo by Cytonn Photography from Pexels
Photo by Andrea Piacquadio from Pexels


## Acknowledgement

Special thanks to my mentor Jonathan Munz for his guidance and advises through this project and also projects.
I also want to thank my personal tutor Yeku Chetat for his patience, taking time to explain and answer my many questions.

I recieved inspiration and references from the following sources:
* [Hygglo](https://www.hygglo.se/)
* [Blocket](https://www.blocket.se/)
* [Jiji](https://jiji.ng/)