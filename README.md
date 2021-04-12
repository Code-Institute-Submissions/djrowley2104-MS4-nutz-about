# Nutz About Hardware
## Introduction
### I decided to follow the Boutique ADO mini project closely in order to make the process much easier for me, I have lost to learn about coding and this project has been the most daunting due to the scale and complexity of the mile stone project.
### I have designed this site to give the hardware shopper the ability to buy hardware products.
### The site could be further developed to show more hardware items, and add more detailed searches and maybe add a deal of the week function. Due to not having the time I have not added any deals.
# Site Goals
## The site design
### The site is designed to be clear and uncluttered, allowing the users to find products and purchase them with ease. The site does not have many products but once the mechanics of getting the product to view and then transferring them from the development area to the final deployed site have been proven. Adding more products and developing the site is just more of the same, I decided to only add 20 ish products to the project.
# UX / User Experience
## First Time Visitor Goals
### As a first time visitor, I want them to be able to be able to, either;  login and create an account easily or if they want to enter the site without an account. The users are told that having an account will make the purchase easier and quicker, but should they choose not to create an account that is fine.
### Once logged in (or not), the users need to be able to find items for sale. They can then navigate easily to the items to look at and easily find the right one to purchase, and add them to their shopping bag. 
### The products should be displayed easily and sorting various types of product must be easy, they should be able to sort via price rating or alphabetically as required.
### The amount they have spent should be clearly displayed and any discounts on postage should be clearly shown.

## Returning User Goals
### As a Returning user, I want them to be able to find the type of product and then find exactly what they want and then they want to easily be able to buy items quickly.
### The returning user is able to log in and to see and review their account profile.
### The returning user should be able to review their purchase history and account details as required, and amend the account details if need.
### The products should be displayed easily and sorting various types of product must be easy, they should be able to sort via price rating or alphabetically as required, allowing for differing users as not all people think in the same way, offering differing way to view products is essential to making their experience of the site a pleasant one and one they want to keep on doing.
### The amount they have spent should be clearly displayed and any discounts on postage should be clearly shown.
## User Goals
### Regardless of the type of user some of the goals will be the same, users will 


# Design / Features
## The site has been designed allow users to see hardware items for sale and to navigate to the required item quickly and easily. 
## When the site is opened the users are shown a hero image showing nuts and bilts, this gives then another clue as to what the site is all about. After logging on the user is taken to the Products page where they are able to search though all the products or filter their searchs via the differing manu options.
## Users entering as guests, are not taken directly to the Products pages, this is done deliberately, as they were told on entering the site that the experience would be slower and more painful if they had accounts.
## Products can be reviewed, updated, deleted and new ones added once again only by the Admin. This has been amended to allow a Product Manager to login and only review, amend, add and remove products. This allows the main admin to be done by the site administrator and product admin to be done by the Product Manager. The product manager enters the product admin section via the Product Manager Tab that is displayed in their account profile section, their login details are;
* User name: product_manager
* Login: cbr601&&
* The Admin super user is: djrowley@hotmail.co.uk
* admin password is: cbr601&&
## The Product manager will be able to amend the products only, but the admin super user has the power to manage everything on the site.
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
### During the testing the site in the deployed project and adding more products, I found that adding a product called Alan Bolts, I found that once I’d added the product it did not show when I searched for allen bolts, but did show when I searched for products. This turned out to be an error in the category name in the search href URL, easy fix.
### I have run through the site’s menus in both the larger screens and the mobile screens to be sure they work as they should. I have found that my product admin link takes the administrator to the admin section perfectly, but it does not have a back button the enable the administrator to return to the products page of the site and see the changes to check how they look and function.
### I have also noticed during the testing of the deployed site that he link to the hero image (bolts.png) does not load, but works fine in the GitPod environment, this points to the links to the media location not being correct or the bolts.png missing, to correct this I have added the https://nutzabouthardware.s3.amazonaws.com/media/bolts.png.
### Webhooks seem to fail, they were just returning a 301, but now I get a 500 server error, I have changed the webhoook key, removed them from setting s.py add them to env.py and the environment variables in Heroku. Just fixed it, https://nutzabouthardware.herokuapp.com/checkout/wh needs to be https://nutzabouthardware.herokuapp.com/checkout/wh/ once the change was made it all worked correctly.
### After the final lesson I tried to sort out the Flake 8 issues, most of them were naming conventions that were too long, I was able to shorten and clean up, but the access keys were not really suitable to shortening, so I elected to leave them.
# Known Bugs 
##  None that I know of the site is fully operational, I think. But you guys will find any errors I have made for sure.
# Deployment
## Initial Development
### After running out of free time in GitPod, I was advised to contact student services, they added me to team unlimited, which was a god send for this project as I needed so much time to get the project working correctly. I did initially get the site working locally, but once I was able to get unlimited access to GitPod I no longer needed to do this, it was going to be hard to keep control of the status of the site and possibly loose work if I had two places to store my work.
## Deployment locally onto Windows
### After getting this working I decided I was going to use this method as it would reduce my GitPod development time. But after getting access to team unlimited, I then decided in order to keep the chances of making issue errors by developing in effect two sites. I decided to only use GitPod as I now had unlimited development time.
## Migration of Images to AWS S3
### Setting up AWS worked as per the lessons; open an account, Setup IAM, Set up S3, Creating the policies in S3, Uploading images. All these were very easy and following the lessons really made it all work very smoothly.
### I also added the products and additional images via the product admin from within the deployed app in Heroku, this added the images to S3 automagically and saved me more time and reducing errors by doing the manual deployment from GitPod to Heroku and creating the json files again.
## Deployment to Heroku
### Deployment to Heroku, seemed easy as after following the lessons it seemed that the builds were successful, I had been lulled into a false sense onsuccess by seeing that the builds were successful, BUT once I tried to open the app in Heroku, that’s when it all went wrong. Naming conventions were not followed, files names were incorrect.
### Setting up Heroku
1.	To set up, the Heroku app
2.	Go to the Heroku website at Heroku com.
3.	Click “new” to create new app. Give the new app a name, and choose the closest region.
4.	From the “Resources” tab, under the add-ons section of the page, type; “Postgres” this will deisplay the options available, from the dropdown menu select the “posrtgres” option with the Heroku icon.
5.	Once selected this will display the submit order page, select the “free plan”.
6.	To use Postgres go back to gitpod and install dj_database_url, and psycopg2; 
* Type; “pip3 install dj_database_url” 
* Type; “ pip3 install psycopg2-binary”
7.	Now to freeze the requirements type; “pip3 freeze > requirements.txt”
8.	This ensures Heroku installs all our apps requirements when we deploy it.
9.	To setup the stores new database go to settings.py, type; “import dj_database_url” under the “import os” text.
10.	Then down in the databases setting, comment out the default configuration, replacing it with a call to dj_database_url.parse, type;  “DATABASES = {     'default': dj_database_url.parse (‘’)}”
11.	Add give it the database URL from Heroku in-between the comments ‘’. Which you can get from your config variables in the Heroku app settings tab and copying and pasting them.
12.	Save the settings.py file, connect to our new Heroku database and run migrations.
13.	To see which migrations have not been setup, type  “python3 manage.py showmigrations”.
14.	To migrate the new settings, Type “python3 manage.py migrate”
15.	It will apply all those migrations and get our database all set up. Now to import all our product data, we can use our fixtures again by first loading in the categories and then the products.
*** Note:-	It is important to do them in that order because the products depend on the categories already existing
16.	To load the categories, type: “python3 manage.py loaddata categories”.
17.	To load the products, type: “python3 manage.py loaddata products”.
18.	To create a superuser, type;  “python3 manage.py createsuperuser” and follow the instructions.
### Create the Profile
1.	Install unicorn, type: “pip3 install gunicorn” 
2.	Now to freeze the requirements type; “pip3 freeze > requirements.txt”
3.	Now create a new file called Procfile in the section that  contains the requirements.txt file. It is important that the Procfile has a uppercase P, this tells Heroku that it needs to read this file.
4.	Inside the Procfile, type: web: gunicorn filename.wsgi:application. The file name must be the name of the folder where the main app is located.
5.	By using Heroku config set, disable type; “heroku config:set DISABLE_COLLECTSTATIC=1 –app= nutzabouthardware”, this will stop Heroku trying to collect static files when deploying.
6.	Note:-	Or you can use DISABLE_COLLECTSTATIC=1
7.	Next add the hostname of the Heroku app to allowed hosts in settings.py, type:
8.	“ALLOWED_HOSTS = ['djr21-botique-ado.herokuapp.com', 'localhost']”
9.	Then push to Heroku master to deploy to Heroku, type; “git push heroku master”
10.	To deploy on Heroku, Type; “heroku git:remote -a filename” The filename must be the name of the project in GitHub.
### Setting up AWS
1.	Navigate to aws.amazon.com, either open a new account or login to an AWS account.
2.	Type is s3 in the search bar, or finding it through the services menu.
3.	Open s3 and create a new bucket, this will be used to store our files.
4.	Click create bucket.
5.	First on the properties tab turn on static website hosting, this will give a new endpoint that can be used to access from the internet.
6.	Click save.
7.	Now on the permissions tab make three changes;
* First paste in a coors configuration which is going to set up the required access between our Heroku app and this s3 bucket. On the bucket policy tab select, policy generator so we can create a security policy for this bucket.  Select policy type “s3 bucket policy”, to allow all principals use a star.
* Allow access to all resources in this bucket, add a slash and * at the end of the resource key, and then click save policy.
* From the Public Access section set the list objects permission for everyone, and click save changes.
### Setting IAM
1.	From the services menu and open IAM
2.	To create a group, click groups then create a new group called “filename”, Filename is whatever name you need.
3.	Click next step.
4.	Create group.
5.	To create the policy to access the bucket click “policies” and then “create policy”.
6.	Click the JSON tab and then select import managed policy which will let us import one that AWS has pre-built for full access to S3, search for “S3” and then import the “S3 full access policy”.
7.	Now here we don't actually want to allow full access to everything we only want to allow full access to our new bucket and everything within it. So get the bucket “ARN” from the bucket policy page in “S3”, copy it.
8.	And paste that in “[“*”]”, using the code [“ARN”, “ARN/*”], now all s3 three actions are allowed both in the bucket itself and on everything in it.
9.	Now click “review policy”.
* Give it a name and a description,
* Click the review “review” button,
* And then click the “create policy” button.
10.	This takes us back to the policies page where we can see our policy has been created successfully.
11.	A attach the policy to the group;
*From “groups”, click my manage boutique-ado-group,
* click “attach policy”,
* Search for the policy we just created by typing part of the name and select it,
* Click “review”,
*And click “attach policy”,
* Finally I'll create a user to put in the group,
* On the user's page, I'll click add user,
* Create a user named boutique-ado-staticfiles-user,
* Select them programmatic access,
* Select next,
* Now put the user in the group. Which as you can see here has our policy attached.
* We don't need to change anything else.
* Click through to the end and then click “create user”.
12.	Now download the CSV file which will contain the users access key and secret access key Which we'll use to authenticate them from our Django app, by clicking the “Download CSV File” button.
13.	To connect django to it, istall two new packages, using “pip3 install boto3” and “pip3 install django-storages”
14.	Freeze those into the requirements.txt file so they get installed on Heroku when we deploy, type: “pip3 freeze > requirements.txt”.
15.	Add storages to the installed apps since django will need to know about it.
16.	To connect Django to s3 we need to add some settings in settings.py to tell it which bucket it should be communicating with. Use the following code;
* if 'USE_AWS' in os.environ:
   * #Bucket Config
    * AWS_STORAGE_BUCKET_NAME = 'djr21-botique-ado'
    * AWS_S3_REGION_NAME = 'EU (London) eu-west-2'
    * AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    * AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    * AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    * #Static and media files
    * STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    * STATICFILES_LOCATION = 'static'
    * DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    * MEDIAFILES_LOCATION = 'media'
    * #Override static and media URLs in production
    * STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    * MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
***Note:-	Adding the access and secret keys from the CSV file that was stored from AWS.
17.	Go to Heroku and add our AWS keys to the config variables, these all come from the CSV file that was created earlier.
18.	While here let's also remove the disable “collectstatic variable” click the delete option.
19.	Back in our settings file. We need to tell django where our static files will be coming from in production. This done using an F string so the bucket name from above will be interpreted and added to generate the appropriate URL.
20.	The next step is to tell django that in production we want to use S3 to store our static files whenever someone runs collectstatic. That we want any uploaded product images to go there also.
21.	To do that create a file called “custom_storages”, use code;
* from django.conf import settings
* from storages.backends.s3boto3 import S3Boto3Storage
* class StaticStorage(S3Boto3Storage):
*    location = settings.STATICFILES_LOCATION
* class MediaStorage(S3Boto3Storage):
*    location = settings.MEDIAFILES_LOCATION
	
	
	
	
	
	
	
	
	
22.	Go to Settings.py
23.	Tell it that for static file storage we want to use our storage class we just created, the location it should save static files is a folder called static.
24.	Then do the same thing for media files by using the default file storage, and media files location settings.
25.	To make sure it works, all we have to do is add all these changes. Commit these changes in GitPod to will trigger the automatic deployment to Heroku.
### Deployment of project to Heroku
1.	Create a new folder in AWS S3 and call it media.
2.	Open the media folder, click upload. Add files images you want to upload.
3.	Next and under manage public permissions select grant public read access to these objects.
4.	Click next through to the end here, then click upload
5.	First we haven't confirmed the email address for our superuser on the Postgres database yet. So we need to do that in the Django admin. 
6.	Finally add the stripe keys to the Heroku config variables.
7.	Clicking developers. And then API keys.
8.	In Heroku, I'll add them as config variables.
9.	Now create a new webhook endpoint;
* The current one is sending webhooks to our gitpod workspace
* Navigateg to webhooks in the developer's menu, and type “URL of your Heroku app, followed by /checkout/WH
* Select receive all events and add endpoint.
10.	Now reveal our webhooks signing secret key, and add that to our Heroku config variables.
### The above step were needed to deploy the project, but unbeknown o me I had forgotten to do some of them correctly.
### After some testing times, I found that; the file name of the Procfile had to have an uppercase “P”, this allowed Heroku to recognise that it was a file that it needed to use during the build process. Plus the name inside the Procfile needed to be the name where the settings.py file was stored not the project name in Heroku. 
### Once these little issues were sorted the builds really worked and the app was viewable. BUT no products were displayed, so onto the next problem, “Getting the products into Heroku”, see below;
## Getting products into Heroku
### This turned out to be a more complicated operation and not as automated as I’d hoped for. First thing is to create the json file containing the products. This took several steps; 
1. Firstly I had to type; “python3 manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json” to create the json file. 
2. Next I had to populate the file, for this I had to then type; “python3 manage.py loaddata db.json”. Json file created and populated.
### After the file was created the json file had to be renamed to products.json and stored in the fixtures directory. The next steps were;
1. Loading of the json file into Heroku. For this I had to type; “heroku run python3 manage.py loaddata products.json” this loaded the products data into the heroku db. 
2. After another git push to trigger a deployment to Heroku and a new build process in Heroku, the products were now viewable in Heroku.
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




