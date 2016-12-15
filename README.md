# JobStat

Protótipo da plataforma JobStat: Inteligência do mercado de trabalho de TI
Demo: [http://ryanom.github.io/jobstat/index.html](http://ryanom.github.io/jobstat/index.html)

## Tecnologias BackEnd
1. **pip** para gerenciar as dependências BackEnd do projeto
2. **Python** para os scripts
3. **PhantomJS e Selenium** para simular um navegador web
4. **BeautifulSoup** para a extração de dados
5. **GitHub** para hospedar os resultados JSON



## Tecnologias FrontEnd
1. **Bower** para gerenciar as dependências FrontEnd do projeto
2. **Gulp.js** para automatizar tarefas de deploy do Portal e compilar arquivos **Sass**
3. **Bootstrap** framework FrontEnd para site responsivo
4. **Sass** para facilitar a estilização do site
5. **Font-awesome** use de ícones interpretados como fonte
6. **HighCharts.js** para os gráficos
7. **DataTable** para as tabelas dinâmicas
8. **Select2.js** para os inputs de select dinâmicos
9. **GitHub Pages** para hospedar o portal  

## Instalação (somente sistemas Unix/OSX)

Verifique que seu sistema tem pip, python, npm e virtualenv instalados.

Baixe o repositório git:
```
$ git clone https://github.com/RyanOM/jobstat.git
```

Acesse a pasta jobstat:
```
$ cd jobstat
```

## Passo a Passo BackEnd

Acesse a pasta jobstat_backend:
```
$ cd jobstat_backend
```

Crie um virtualenv para a instalação das dependências:
```
$ virtualenv jobstatenv
$ source jobstatenv/bin/activate
```

Instale as dependências:
```
(jobstatenv) ~$ pip install -r requirements.txt
```

Execute os crawlers:
```
(jobstatenv) ~$ cd crawlers
(jobstatenv) ~$ python apinfo_page_crawler.py
(jobstatenv) ~$ python ceviu_crawler.py
(jobstatenv) ~$ python netcarreiras_crawler.py
(jobstatenv) ~$ python trampos_api_crawler.py	
```
Os dados raspados serão salvos na pasta: crawled_data

Execute os normalizers:
```
(jobstatenv) ~$ cd normalizers
(jobstatenv) ~$ python apinfoParser.py
(jobstatenv) ~$ python ceviuParser.py
(jobstatenv) ~$ python netcarreirasParser.py
(jobstatenv) ~$ python trampos_jsonParser.py
```
Os dados normalizadas serão salvos na pasta: normalized_data

Execute os analyzers:
```
(jobstatenv) ~$ cd analyzers
(jobstatenv) ~$ python job_offer_counter.py
(jobstatenv) ~$ python skill_analyzer.py	
```
Os resultados serão salvos na pasta: analyzed_data


## Passo a Passo FrontEnd

Acesse a pasta jobstat_frontend
```
$ cd jobstat_frontend
```

Baixe as dependências
```
$ npm install --save-dev gulp
$ bower install
```


Execute o projeto
```
$ gulp dev
```


## Grupo
Ryan David O'Mullan