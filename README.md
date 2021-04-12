# Nutz About Hardware
## Introduction
### I decided to follow the Boutique ADO mini project closely in order to make the process much easier for me, I have lost to learn about coding and this project has been the most daunting due to the scale and complexity of the mile stone project.
### I have designed this site to give the hardware shopper the ability to buy hardware products.
### The site could be further developed to show more hardware items, and add more detailed searches and maybe add a deal of the week function. Due to not having the time I have not added any deals.

# Site Goals
## The site design
### The site is designed to be clear and uncluttered, allowing the users to find products and purchase them with ease. The site does not have many products but once the mechanics of getting the product to view and then transferring them from the development area to the final deployed site have been proven. Adding more products and developing the site is just more of the same.


# UX / User Experience
## First Time Visitor Goals
### As a first time visitor, I want them to be able to be able to, either;  login and create an account easily or if they want to enter the site without an account. The users are told that having an account will make the purchase easier and quicker, but should they choose not to create an account that is fine.
### Once logged in (or not), the users need to be able to find items for sale. They can then navigate easily to the items to look at and easily find the right one to purchase, and add them to their shopping bag. 
### The products should be displayed easily and sorting various types of product must be easy, they should be able to sort via price rating or alphabetically as required.
### The amount they have spent should be clearly displayed and any discounts on postage should be clearly shown.

## Returning User Goals
### As a Returning user, I want them to be able to find the type of product and then find exactly what they want and then they want to easily be able to buy items quickly.
### The returning user is able to log in and to see and review their account profile.
### The returning user should be able to review their purchase history and account details as required.
### The products should be displayed easily and sorting various types of product must be easy, they should be able to sort via price rating or alphabetically as required, allowing for differing users as not all people think in the same way, offering differing way to view products is essential to making their experience of the site a pleasant one and one they want to keep on doing.

# Design / Features
## The site has been designed allow users to see hardware items for sale and to navigate to the required item quickly and easily. 
## When the site is opened the users are shown a hero image showing nuts and bilts, this gives then another clue as to what the site is all about. After logging on the user is taken to the Products page where they are able to search though all the products or filter their searchs via the differing manu options.
## Users entering as guests, are not taken directly to the Products pages, this is done deliberately, as they were told on entering the site that the experience would be slower and more painful if they had accounts.
## Products can be reviewed, updated, deleted and new ones added once again only by the Admin. This has been amended to allow a Product Manager to login and only review, amend, add and remove products. This allows the main admin to be done by the site administrator and product admin to be done by the Product Manager. The product manager enters the product admin section via the Product Manager Tab that is displayed in their account profile section, their login details are;
* User name: product_manager
* Login: cbr601&&
## Nuts and bolts can have sizes added to them from the size selector, this will apply a different price per size, the prices are managed from the admin section of the Django db, the prices are added to the grand total and the free postage countdown, so the site works as it should.  I have elected to only add sizes to one nut, but he mechanics are the same and I could apply sizes to any products that needed them, but to save time as I seem to be running out of it rapidly I have only added ti the one product.

## Colour Scheme
### I decided to use a light and uncluttered page design to allow the user to focus on the products, the users will only be interested in the price and the type and size of the products, they will not want to be mislead via clever flashing images, so I have kept it simple.
## Typography
### Standard fonts from Bootstrap have been used, I have no need to over complicate this project, I feel standard san serif font is easier to read and therefore better for the user. No need to keep the users confused with stupid hard to read font types, if I did that the users would not be users for long.
## Imagery
### Imagery is important. The images used where all taken from Google searches and then adapted to my requirements using MS Paint. There are better packages to use to edit images but MS Paint is free and produces good results.
## Home Page Wireframe - View
### Below you can see the desktop wireframe, which was designed to show the path the user shuld take to get into the site;
<img src="/media/homescreenwireframe.png">;

### The user should login or continue as a guest, either option is available, however the proceed as a guest option does have some draw backs mainly in the time it takes to checkout.
## Products Screen
### The products screen has been designed to show all the products in a grid of four products on larger screens, and one product per line on small screens
<img src="/media/productsscreen.png">;

## Mobile Wireframe - View
### Below you can see the mobile device wire frame, this follows the exact same logic, but shows one product per line on the smaller mobile screen, the products will be displayed in a burger, and once clicked on they will display;
<img src="/media/mobilescreen.png">;
## Features
### Responsive on all device sizes
#### I checked the site out using google chrome and it was responsive, using the inspect feature. Having used Bootstrap before I am confident with some small tweaks here and there that the standard Bootstrap elements work well on all screen sizes.

# Interactive elements

## Technologies Used
### Languages Used
* HTML
* JavaScript
* CSS3
* DNSPYTHON
* Django
## Relational Databases
* MySQL
* Postgres
* Plus Strip payments
## Frameworks, Libraries & Programs Used
* Bootstrap
### Bootstrap was used to assist with the responsiveness and styling of the website.
* Font Awesome:
### Font Awesome was also used as the icon provider.
* GitPod
### GitPod was used for version control by utilizing the Gitpod terminal to commit to Git and Push to Github
* GitHub.
### GitHub is used to store the projects code after being pushed from Gitpod.
* PC Paint
### PC Paint was used to create the wireframes during the design process this was due to the free version of Balsmic running out, but in fairness it worked as well and was able to show the basic page layout.
* AWS; S3 and IAM
### These were used to store images and control access.
* Stripe Payment
### Stripe handles the payment system.
* Allauth
### Created the management of messages that helped to confirm actions performed within the site, this is essential to help the user understand that they have been successful in doing an action on ths site.

# Testing
## During initial testing the products when scrolling on the product screen would show in the header, to rectify this I used the bg-white class to turn the header background white and therefore stop this error.
## After creating the login page, I wanted the user to be able to; if they were logged on already, or after logging on, to be directed to the products page, this turn out to be an easy fix. From the setting.py file I found the LGIN_REDIRECT_URL and added /products/ to it, now the user is directed to the products page after logging on. Even if they were already logged in the link will also be sent to the products pages. But should they enter as a guest they get sent to a blank page, this is designed to further increase/cement the fact that entering without an account is slower and less of a smooth experience.
## Testing is on-going during the whole build process as certain changes effected the way the site functioned or did not function. Basically each app added to the GitPod build added a chance for things to go wrong, and normally they did, which was handy as it helped me to understand some of the error resolving part of the process.
## During the design process I decided that I wanted to add differing prices for the different sizes of the bolts and nuts. This was achieved by adding a class in django products called product sizes, this introduces the sizes and the different prices per size. The prices and sizes are linked to the product, this allows differing prices/sizes to be added for each product, helping to make the site a more realistic one. 
## There were several challenges getting the prices to show up and work on the site, but after some testing everything turned out just fine.
## Getting the mobile top header to display correctly took some effort and head scratching, when the screen size was small below 992 px, both headers were displayed, after lots of searching I found that the “d-none d-lg-flex” classes needed to be applied to the base.html header in order to stop it being displayed. This took some finding, but once added the site worked as it should have.
## First time user, will either create an account or enter as a guest, either option will get them to the products page, and they can select options as they want. They can search the products page, this can be searched via the all products tab or further refined using the nuts, bolts or screws tabs.

## Returning Visitor Goals
### A returning visitor would need to be able to see the products quickly, this is why after logging on they are directed to the products page, this can be searched via the all products tab or further refined using the nuts, bolts or screws tabs.

## Frequent User Goals
### As a Frequent User, I decided that they would need access to see their past orders and to be able to find the items they want easily. The products page is displayed on logging into the site, this displays everything that is on the site. Various searches can be selected, these can be types of nuts and bolts or materials they are made from.

## Further Testing

### I have run through the site’s.

# Known Bugs 
##  

# Deployment

## Initial Development
### After running out of free time in GitPod, I was advised to contact student services, they added me to team unlimited, which was a god send for this project as I needed so much time to get the project working correctly. I did initially get the site working locally, but once I was able to get unlimited access to GitPod I no longer needed to do this, it was going to be hard to keep control of the status of the site and possibly loose work if I had two places to store my work.
## Deployment locally onto Windows
### After getting this working I decided I was going to use this method as it would reduce my GitPod development time. But after getting access to team unlimited, I then decided in order to keep the chances of making issue errors by developing in effect two sites. I decided to only use GitPod as I now had unlimited development time.
## Migration of Images to AWS S3
### Setting up AWS worked as per the lessons; open an account, Setup IAM, Set up S3, Creating the policies in S3, Uploading images. All these were very easy and following the lessons really made it all work very smoothly.
## Deployment to Heroku
### Deployment to Heroku, seemed easy as after following the lessons it seemed that the builds were successful, I had been lulled into a false sense onsuccess by seeing that the builds were successful, BUT once I tried to open the app in Heroku, that’s when it all went wrong. Naming conventions were not followed, files names were incorrect.
### After some testing times, I found that; the file name of the Procfile had to have an uppercase “P”, this allowed Heroku to recognise that it was a file that it needed to use during the build process. Plus the name inside the Procfile needed to be the name where the settings.py file was stored not the project name in Heroku. 
### Once these little issues were sorted the builds really worked and the app was viewable. BUT no products were displayed, so onto the next problem, “Getting the products into Heroku”, see below;
## Getting products into Heroku
### This turned out to be a more complicated operation and not as automated as I’d hoped for. First thing is to create the json file containing the products. This took several steps; 
1. Firstly I had to type; “python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json” to create the json file. 
2. Next I had to populate the file, for this I had to then type; “python3 manage.py loaddata db.json”. Json file created and populated.
3. After the file was created the json file had to be renamed to products.json and stored in the fixtures directory.
4. Next loading of the json file into Heroku. For this I had to type; “heroku run python3 manage.py loaddata products.json” this loaded the products data into the heroku db. 
5. After another git push the products were now viewable in Heroku.
### This process would need to be repeated each time the django db in gitpod was changed in order for the changes to appear in the app in Heroku. As this is a long winded process I elected to only edit the data in the admin section of the Heroku app (as so I understand, have all the other students and tutors in the past).


# Credits
## Code 
### I decided to have a hero image on the login screen of my site. This gave the user more understanding of what the site was about. Once logged in or entering as a guest the users of the site were able to search for products and buy them, either as a guest or having an account. 
### I found code for the project from the Boutique ADO  project, which has been invaluable to helping me understand the logic and to getting my site to perform in a similar way to the project, with some subtle differences. 
### I also used the tutors from the code institute to help with some problems. Of which there were many and at times contacting the tutors was a very helpful and I normally got the problem resolved.
## Bootstrap
## I used the Bootstrap Library throughout the project mainly to make site responsive using the Bootstrap Grid System.
## Bootstrap has been invaluable in making a responsive and useable website.

# Content
## Most of the content is generated from the GitPod and linked to the Django db.

# Media
## All Images were created from google searches, using MS Paint to edit them to create the collage of pictures. 
## The other images which had urls to the image and were found using Google.
# Acknowledgements
## My Mentor for continuous helpful feedback. I was able to learn so much from our short meetings, they have been invaluable to me. My mentor was able to help me think differently and to use different tools and code that were able to help me with the project. Without his help I would still be pulling my hair out, I cannot thank him enough. I only hope I have not let him down with my readme file.
## The Boutique ADO project, this was invaluable to getting my project working correctly, and helping me understand some of what I was doing, the lessons were extremely usefull to me during the initial set up and testing of the project.
## Tutor support at Code Institute for their support, while I have not used them for any of my projects until now, when I contacted them regarding this project they were very helpful. And after some hard work on their part able to understand my thinking and help solve the problem. So thank you for your understanding and help.
## Code institute for putting this course together, each project has helped me grow and given me a better understanding of what I have learnt so far. I don’t really ever want the journey to stop, so if I can proceed to the final segment it will be great, BUT, also I feel I will need to continue on some more courses.....
## Can we have access to the course material after the course has finished?




