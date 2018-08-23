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

Verifique que seu sistema tem [npm](https://nodejs.org/en/download/), [pip](https://pip.pypa.io/en/stable/installing/) e [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) instalados.

Após instalar todas as dependências, baixe o projeto:
```
$ git clone https://github.com/RyanOM/jobstat.git
```

Acesse a pasta do projeto jobstat:
```
$ cd jobstat
```

## BackEnd - Passo-a-Passo

Acesse a pasta `jobstat_backend`:
```
$ cd jobstat_backend
```

Estrutura `jobstat_backend`

![alt text](https://s28.postimg.org/eiq89uzcd/Screen_Shot_2016_12_15_at_4_23_20_PM.png "Logo Title Text 1")


Crie uma virtualenv e ative-a para que, na sequência, todas as dependências serem instaladas:
```
$ virtualenv jobstatenv
$ source jobstatenv/bin/activate
```

Instale as dependências:
```
(jobstatenv) ~$ pip install -r requirements.txt
```

Para executar os *crawlers* a partir da pasta `jobstat_backend`:
```
(jobstatenv) ~$ cd crawlers
(jobstatenv) ~$ python apinfo_page_crawler.py
(jobstatenv) ~$ python ceviu_crawler.py
(jobstatenv) ~$ python netcarreiras_crawler.py
(jobstatenv) ~$ python trampos_api_crawler.py	
```
Os dados raspados serão salvos na pasta: `jobstat_backend/crawled_data`

Para executar os *normalizers* a partir da pasta `jobstat_backend`:
```
(jobstatenv) ~$ cd normalizers
(jobstatenv) ~$ python apinfoParser.py
(jobstatenv) ~$ python ceviuParser.py
(jobstatenv) ~$ python netcarreirasParser.py
(jobstatenv) ~$ python trampos_jsonParser.py
```
Os dados normalizadas serão salvos na pasta: `jobstat_backend/normalized_data`

Para executar os *analyzers* a partir da pasta `jobstat_backend`:
```
(jobstatenv) ~$ cd analyzers
(jobstatenv) ~$ python job_offer_counter.py
(jobstatenv) ~$ python skill_analyzer.py	
```
Os resultados serão salvos na pasta: `jobstat_backend/analyzed_data`


## FrontEnd Local - Passo-a-Passo

Acesse a pasta `jobstata/jobstat_frontend`:
```
$ cd jobstat_frontend
```

Baixe todas as dependências do portal:
```
$ npm install --save-dev gulp
$ bower install
```


Execute o projeto:
```
$ gulp dev
```

Se por acaso ocorrer, durante o processo ocorrer algum erro, execute o seguinte comando:
```
$ npm cache clean
$ npm install
```

E finalmente, acesse o portal no seguinte endereço local: [http://localhost:3000/html/pages/home.html](http://localhost:3000/html/pages/home.html)
