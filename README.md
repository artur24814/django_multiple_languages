# django_multiple_languages
<img src="https://github.com/wsvincent/awesome-django/raw/main/assets/django-logo.svg">
<h2>Contents</h2>
<ul>
   <h3><a href="#info"><strong>Info</strong></a></h3><p>Information about the resources used in this project</p>
   <h3><a href="#django_multiple_languages"><strong>Django multiple languages</strong></a></h3><p>Website for booking screenings at the cinema</p>
   <h3><a href="#clone_project"><strong>Clone and Run a Django Project</strong></a></h3><p>how run projects in your computer</p>
</ul>
<hr>

<details><summary id="info" style="font-size: 30px;"> INFO</summary>
<h4>Information about the additional library, external Api used in this project and general information</h4>

<strong>The gettext module</strong> provides internationalization (I18N) and localization (L10N) services for your Python modules and applications. It supports both the GNU gettext message catalog API and a higher level, class-based API that may be more appropriate for Python files.

<strong>use the django-modeltranslation package</strong> here which will create different columns for attributes that are marked for translation. The code is very similar to what you write for django-admin for any data model in your app.

</details>

<hr>


<center><h1 id="django_multiple_languages"> Django multiple languages <span style='font-size:80px;'><img src="https://img.icons8.com/dusk/64/000000/language.png"/></span></h1></center>

<h3>set up your computer</h3>
<p>to start using internationalization instal gettext in your computer in global environment</p>
  <section>
   <p>Use<code>sudo art-get install gettext</code> in Ubuntu</p>
   <p>Use<code>brew install gettext</code> in macOS</p>
   <p> In Windows Download the following zip files from the GNOME servers http://ftp.gnome.org/pub/gnome/binaries/win32/dependencies/ or from one of its mirrors;
    X is the version number, we are requiring 0.19.8.1 or higher.</p>
    <p><code>gettext-runtime-X.zip</code></p>
    <p><code>gettext-tools-X.zip</code></p>
    <p>Extract the contents of the bin\ directories in both files to the same folder on your system (i.e. C:\Program Files\gettext-utils)</p>

    Update the system PATH:
        Control Panel > System > Advanced > Environment Variables.
        In the System variables list, click Path, click Edit.
        Add ;C:\Program Files\gettext-utils\bin at the end of the Variable value field.
  <p>You may also use gettext binaries you have obtained elsewhere, so long as the following command works properly: </p>
  <code>xgettext --version</code>
  <p>Do not attempt to use Potion with a gettext package if the command <code>xgettext --version</code> entered at a Windows command prompt causes a popup window saying "xgettext.exe has generated errors and will be closed by Windows".</p>
  </section>

<h3>set up your django project</h3>
<h5>settings.py</h5>
<section>
<p>Start from import <code>from django.utils.translation import ugettext_lazy as _</code></p>


then in MIDDLEWARE:


     MIDDLEWARE = [
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.locale.LocaleMiddleware',
        'django.middleware.common.CommonMiddleware',
     ]


Make sure that LocaleMiddleware comes after SessionMiddleware and before CommonMiddleware it is important!

With the settings in place, we’ve told Django the information that it needs to enable translations.

 If you set this to False, Django will make some optimizations so as not to load the internationalization machinery. Make sure it is set to True if you want to support localization
  
 `USE_I18N = True`

Set the default language for your site.

   `LANGUAGE_CODE = 'en'`

Provide a lists of languages which your site supports.

    LANGUAGES = [
        ('en', _('English')),
        ('pl', _('Polish')),
    ]

Show to your project where he should find locals languages. To do this add information about this to your project


    LOCALE_PATHS = [
      BASE_DIR / 'locale'
    ]

</section>

<h5>urls.py</h5>

Start from imports 

 `from django.conf.urls.i18n import i18n_patterns`

And to your patterns add i18n_patterns

and add all path which may bee translated

    urlpatterns = [
        path('admin/', admin.site.urls),
    ] + i18n_patterns(
        path('i18n/', include('django.conf.urls.i18n')),
        path('', HomePage.as_view(), name='home'),
        prefix_default_language=False
    )

if you set `prefix_default_language=False` when your site are in default language in url will show only particularly url without active language

not `https://www.site.com/en/page/` -> `https://www.site.com/page/`

<h5>views.py</h5>

start from import again

`from django.utils.translation import gettext as _`

then create texts for translate

```


#navbar
language = _('Language')

home = _('Home')

#bodu
card_header = _('Warsaw')

card_title = _('Warsaw officially the Capital City of Warsaw')

```

and add this text to context to rendering ia a page

```
context = {
            'Language': language, 
            'card_header': card_header,
            'card_title': card_title,
        }
        return render(request, 'home.html', context)

```

<h5>In templates</h5>

```
{% load i18n %}

<nav>
  <div>{% translate 'Language' %}</div>
</nav>

  <h1>{% translate 'card_header' %}</h1>
  <p>{% translate 'card_title' %}</p>

```

<h5>Create 'locale' directory</h5>

in root project directory create locale directory 

```
/project/
        core/
        app/
        templates/
        locale/
               en/
               pl/
         manage.py
```

or use `mkdir locale` then `cd locale` + `mkdir en` + `mkdir pl`

<h5>Make messages</h5>

Run command `django-admin makemessages --all --ignore venv` 

part code `--ignore venv` was to ignore virtual environment texts. Not necessary, but it helps to avoid creating many lines of code

django create for as some files

```
/project/
        core/
        app/
        templates/
        locale/
               en/
                  LC_MESSAGES/
                        django.po
               pl/
                  LC_MESSAGES/
                        django.po
         manage.py

```

in 'django.po' and directory with not default language for your project (for my project it was 'pl')

find your text to translating and translate it

```
msgid "Language"
msgstr "Język"


msgid "Home"
msgstr "Główna"


msgid "Warsaw"
msgstr "Warszawa"

msgid "Warsaw officially the Capital City of Warsaw"
msgstr "Warszawa oficjalnie miastem stołecznym Warszawy"
```

Next write command `django-admin compilemessages`

if oll will be ok you must see new binary files in your project

```
/project/
        core/
        app/
        templates/
        locale/
               en/
                  LC_MESSAGES/
                        django.mo
                        django.po
               pl/
                  LC_MESSAGES/
                        django.mo
                        django.po
         manage.py


```

And that's all congratulations!!!

Your website has multiple languages

<img src="https://img.icons8.com/office/30/000000/error.png"/> Attention  ! command which I use `django-admin makemessages --all` and `django-admin compilemessages` may bee another in 
different version of django and maybe different systems, because I saw in another tutorials programmers route 
commands `python manage.py makemessages -l` and `python manage.py compilemessages` if one type of commands not work
try another
 also you can use package the django-modeltranslation here which will create different columns for attributes that are marked for translation. The code is very similar to what you write for django-admin for any data model in your app.


  <hr>
<center><h2 id="clone_project">Clone and Run a Django Project</h2></center>

Before diving let’s look at the things we are required to install in our system.

To run Django prefer to use the Virtual Environment

`pip install virtualenv`

Making and Activating the Virtual Environment:-

`virtualenv “name as you like”`

`source env/bin/activate`

Installing Django:-

`pip install django`

Now, we need to clone project from Github:-
<p>Above the list of files, click Code.</p>
<img src="https://docs.github.com/assets/cb-20363/images/help/repository/code-button.png">

Copy the URL for the repository.
<ul>
<li>To clone the repository using HTTPS, under "HTTPS", click</li>
<li>To clone the repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click SSH, then click</li>
<li>To clone a repository using GitHub CLI, click GitHub CLI, then click</li>
</ul>
<img src="https://docs.github.com/assets/cb-33207/images/help/repository/https-url-clone-cli.png">

Open Terminal.

Change the current working directory to the location where you want the cloned directory.

Type git clone, and then paste the URL you copied earlier.

`$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

Press Enter to create your local clone.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `Spoon-Knife`...<br>
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Install the project dependencies:

`pip install -r requirements.txt`


create admin account (**remember you must be at the main application folder with file manage.py, and do this steps for
each application in this repository!!!!**)

`python manage.py createsuperuser`

then

`python manage.py makemigrations`

then again run

`python manage.py migrate`


to start the development server

`python manage.py runserver`

and open localhost:8000 on your browser to view the app.

Have fun
<p style="font-size:100px">&#129409;</p>


