# JobStat

Prototype of the JobStat platform: IT job market intelligence

Demo: [http://ryanom.github.io/jobstat/index.html](http://ryanom.github.io/jobstat/index.html)

## BackEnd Technologies
1. **pip** to manage Python dependencies
2. **Python** for the scripts
3. **PhantomJS e Selenium** to mimic a web browser
4. **BeautifulSoup** to extract data from the html files
5. **GitHub** to host the JSON results



## FrontEnd Technologies
1. **Bower** to manage dependencies
2. **Gulp.js** to aumotimate the tasks of deployment and compile **Sass**, **JS**, etc
3. **Bootstrap** responsive web framework for the website
4. **Sass** for styling
5. **Font-awesome** for icons.
6. **HighCharts.js** for data visualisation
7. **DataTable** for dynamic tables
8. **Select2.js** dynamic select input fields
9. **GitHub Pages** to host the website

## Installation requirements

System: Unix/OSX
Verify if your system has [npm](https://nodejs.org/en/download/), [pip](https://pip.pypa.io/en/stable/installing/) e [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) installed.

After installing the dependencies, download the project:
```
$ git clone https://github.com/RyanOM/jobstat.git
```

Access the folder of the `Jobstat` project:
```
$ cd jobstat
```

## Backend: Step by Step

Access the folder `jobstat_backend`:
```
$ cd jobstat_backend
```

Structure for `jobstat_backend`

![alt text](https://s28.postimg.org/eiq89uzcd/Screen_Shot_2016_12_15_at_4_23_20_PM.png "Logo Title Text 1")


Create a virtualenv and activate it. Then install all the dependencies:
```
$ virtualenv jobstatenv
$ source jobstatenv/bin/activate
```

Install the dependencies:
```
(jobstatenv) ~$ pip install -r requirements.txt
```

Run the *crawlers* from the `jobstat_backend` folder:
```
(jobstatenv) ~$ cd crawlers
(jobstatenv) ~$ python apinfo_page_crawler.py
(jobstatenv) ~$ python ceviu_crawler.py
(jobstatenv) ~$ python netcarreiras_crawler.py
(jobstatenv) ~$ python trampos_api_crawler.py	
```
The scaped data will be saved in the folder: `jobstat_backend/crawled_data`

Run the *normalizers* from the `jobstat_backend` folder: 
```
(jobstatenv) ~$ cd normalizers
(jobstatenv) ~$ python apinfoParser.py
(jobstatenv) ~$ python ceviuParser.py
(jobstatenv) ~$ python netcarreirasParser.py
(jobstatenv) ~$ python trampos_jsonParser.py
```
The normalized data will be saved in the folder: `jobstat_backend/normalized_data`

Run the *analyzers* from the `jobstat_backend` folder: 
```
(jobstatenv) ~$ cd analyzers
(jobstatenv) ~$ python job_offer_counter.py
(jobstatenv) ~$ python skill_analyzer.py	
```
The results will be saved in the folder: `jobstat_backend/analyzed_data`


## Local FrontEnd: Step by step

Access the folder `jobstata/jobstat_frontend`:
```
$ cd jobstat_frontend
```

Install all the dependencies of the platform:
```
$ npm install --save-dev gulp
$ bower install
```


Run the project:
```
$ gulp dev
```

If any error occures, try running the following command:
```
$ npm cache clean
$ npm install
```

Finally access the portal going to the following link: [http://localhost:3000/html/pages/home.html](http://localhost:3000/html/pages/home.html)
