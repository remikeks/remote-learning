# REMOTE LEARNING
#### Description:
    Remote Learning is my implementation of a web application which lets users register for free online courses on an institution's website. Languages and frameworks used include: HTML, CSS, Bootstrap, SQL, and Python(Flask). The application consists of an `app.py` file and a `requirements.txt` file in addition to `templates` and `static` subdirectories and a `courses.db` database.

    The file `app.py`, written in Python(Flask), contains the backend source code for the application. The libaries used are listed in the `requirements.txt` file. `app.py` defines three functions:
        * index()
        * courses()
        * register()
    The `index()` function return the homepage of the website; `courses()` returns a page displaying the courses currently being offered by the institution; register() either returns the registration page or the user's profile page, depending on the method by which it is called. It as well provides a backend validation to ensure the user has not (maliciously) overwritten or bypassed a process on the frontend.

    The `courses.db` database contains all the courses currently being offered by the institution, and the approximate duration (in months) it takes to complete each course. The database is to be updated as more courses are introduced.

    The `static` subdirectory contains two files; an image file, `image1.jpg`, which is in fact, the only image contained in the website, as well as a `styles.css` file, containing the sylesheet code used in styling some parts of the markup.

    The `templates` subdirectory contains six(6) .html files:
        * layout.html
        * index.html
        * courses.html
        * register. html
        * profile.html
        * error.html

    The layout.html file contains a markup template which the other files `extend` using jinja syntax.

    The index.html file is the homepage of the website. It contains the name of the institution, as well as basic information about her. In addition to the image displayed, there are two links visible toward the bottom of the page:

        The first link redirects to the courses.html page, which displays a table from the courses database containing the name and estimated duration of each course (in months). A link is provided to return the user to the homepage.

        The second link redirects to the registration page where the user is presented with a form with required input fields to fill. On submission, the user is notified of successful registration and is directed to the profile page where they can see their profile. A link is provided to return to the homepage.

    Assuming the user, somehow, submits the form without filling out one (or more) of the required input fields or selects an option not provided in the registration form, the error.html page is displayed informing the user that there has been an error.