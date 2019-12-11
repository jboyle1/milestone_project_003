### https://milestone-project-003.herokuapp.com/
 
## Milestone Project 3 (Paddy Boyle photography showcase website)

### Initiation

For the Interactive Data-Centric Development Milestone Project (project 3), I have decided to update a website for my client Paddy Boyle. He needs a website that showcases his property photography. I previously designed and developed his old website https://jboyle1.github.io/old-www.pboylephotography.com/ and I think it needs updating to look more contemporay.

### Kickstarter Meeting

After talking with Paddy, we decided on a few main points I found out that he needs different categories for his photo galleries, i.e:

* Architecture
* Commercial
* Property
* Construction 

He would also like an about page, a services page and a contact page.

### Thoughts after the meeting

It seems that Paddy wants a simple showcase website. He would like it to be a corporate looking site with a blue colour scheme. I will be able to reuse a lot of the content from the old site (images, text).

### Main Technology Requirements for Project

#### Required:

* HTML & CSS:

I will be able to use bootstrap to structure and style the front end of the site. The about page, services and contact page should be easy enough to implement with this framework.

* Javascript:

Relevant Bootstrap Javascript could be used for lightbox galleries and carousel.

* Python & Flask:

I think categorized photo galleries would be a good way to implement flask template routing with Python. Also for a navbar base template for every page on the site.

* MongoDB:

I can use the MongoDB DBMS with JSON framework to store images and images data. This will cover the ‘read’ from the CRUD database operations.

* SQLite

I will use SQLite to implement the ‘create, update and delete’ operations from the CRUD database operations. I am going to add a testimonials page where the user can create, read, update and delete a message about a particular showcase.

### Plan 

#### Initial UX/UI Development

* Home page part 1 (nav bar):

A nav bar across the top will be stuck to all pages as a template and also stuck as the user scrolls down the page. It will be fully responsive along with the rest of the site. The nave bar will encompass a logotype, the about section link, a portfolio section link, a prices section link and the contact section link.

* Home page part 2 (load page):

I have had a research into contemporary photography websites and settled on a simple homepage design that shows a carousel with striking images provided by paddy. He will be providing all of the Images for this project. This image will be full width and height. 

* Home page part 3 (about section):

Here I will have paddy write a bio and description of his profession.

* Home page part 4 (portfolio section):

With the use of the MongoDB DBMS I will call data from their servers to populate these four catagory images that link to the galleries.

* Home page part 5 (prices section):

I will use the information from the old site to populate this section in a three column grid.

* Home page part 6 (contact section):

I will use the gmail API to implement a contact form with a bootstrap themed form.

* Gallery pages:

Easch gallery page will have the same nav bar ase all the other pages using flask templating. I will also create a second base page to template all the thumbnail images which will be called from MongoDB. In rows of three the photos will fill the pages. Each showcase will have a Javascript lightbox gallery displaying individual properties inside catagories for example; arhitecture, commercial, property and construction. All of these images are stored in MongoDB.

* testimonials page:

Thw tetimonials page will show a table enabling you to add a testimonial. It will also give the date that it was made. You will have the option to update and delete the message too.

### Wireframe Sketches

I decided to use a bootstrap theme to save time. This is the 'freelancer' template from https://startbootstrap.com/themes/

### Documentation

I decided to use the GitPod IDE for this project because I couldn’t install pymongo in Cloud9. I thought it would be best if I started with the home page first so I could make a template that was consistent throughout the website.

Firstly I created a virtual environment so anything I store will be contained inside this scoped environment. I then Installed the relevant frameworks to VSCode, this included: flask, pymongo, flask-pymongo and dnspython. Then I added app.py to run my python code along with the Procfile and requirements.txt for the modules I would be needing. I then initiated a local git repository and added my progress with an Initial commit.

To make an outline for the entire application I opened up app.py and imported Flask. I then tested it using the relevant routing and the text “Hello World” to be shown in the browser as a test to see if all was running well.

I then created a static folder and a templates folder, adding an index.html file to the templates. Re-routed the index function to open the index,html and tested it using “Hello World two”.

For template inheritance I created a base.html and inserted boilerplate html and the ginger2 code block syntax for the head and the body. Then I added the relevant syntax to the index.html for template inheritance extension. I tested it using the <h1> “Testing” and ran the program.

I used a bootstrap theme from https://startbootstrap.com/ to save time I copied the head and navbar and pasted it into the base.html. This way all pages on the site will have this template. In the index.html I pasted the rest of the code into the flask body code block. I now had a layout for my homepage. I added some bootstrap code for an image carousel and an image layout for the portfolio categories. I used an old contact form from a previous project to save time too. The website seemed to be working well and was fully responsive. The site was looking quite corporate which is what the client wanted. Using the content from the old site I filled in the about section, portfolio section and prices section. I also created a second base.html (base-002.html) which is a template for the separate gallery pages. I added some css styling to the main css file that came with the bootstrap theme to conform with my clients specification. Once I had the layout for the index page and the gallery pages set I needed to add the image.

I used a website called www.imgbb.com to upload all the images for the site. I had all these from his old site. By uploading all these images I gained a url link to each one. I then created individual database collections for each category and property in www.mongodb.com . Inside these collections I created data documents, including a photo name and a URL for each photo.

Using python and Flask I made functions for each gallery that loop through each of their related photo database on MongoDB and show them in the browser. The category galleries were a bit trickier as I need them to link to their respective property galley with a href which I couldn’t do with html, so I added an extra piece of data to each document, a url link that would connect each photo to individual page and added into the flask loop. Once I had all the galleries finished I connected the contact form to the gmail API and got that functioning.

I needed to cover all the CRUD database operations not just read only (images from db). For this I decided to create an add testimonials page for every showcase. I did this by repurposing an application I used for another project (a task manager). By adapting this code I figured out how to make the testimonials page function along with the rest of the routing and database management. Instead of using MongoDB I used SQLite to store inputted data. Users access the testimonials page by clicking on a specific property gallery and clicking on the link above the images marked ‘add a testimonial’.

All my documentation is backed up with regular Git commits. I then deployed the site with Heroku.

I think this project has shown that I am competent in building full-stack websites that use common dataset and the CRUD operations. All the images on the site apart from the carousel are kept in a MongoDB database and are accessed by utilising Python, Flask and pymongo.
