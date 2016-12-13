# JobStat

Protótipo da plataforma JobStat: Inteligência do mercado de trabalho de TI
Demo: [http://ryanom.github.io/jobstat/index.html](http://ryanom.github.io/jobstat/index.html)

## Tecnologias BackEnd
1. **pip** para gerenciar as dependências BackEnd do projeto
2. **Python** para os scripts
3. **PhantomJS e Selenium** para simular um navigador web
4. **BeautifulSoup** para a extração de dados
5. **GitHub** para hospedar os resultados JSON



## Tecnologias FrontEnd
1. **Bower** para gerenciar as dependências FrontEnd do projeto
2. **Gulp.js** para automatizar tarefas do deploy do Portal e compilar **Sass**
3. **Bootstrap** framework FrontEnd para site responsivo
4. **Sass** para styling
5. **Font-awesome** para os icones
6. **HighCharts.js** para os graficos
7. **DataTable** para as tabelas dinamicas
8. **Select2.js** para as select dinamico
9. **GitHub Pages** para hospedar o portal  

## Instalação (somente sistemas Unix/OSX)

Verifique que sua sistema tem pip, python, npm e virtualenv instalados.

Baixe o repositorio git
```
git clone https://github.com/RyanOM/jobstat.git
```

Entra no arquivo jobstat
```
cd jobstat
```

## Passo a Passo BackEnd

Entra no arquivo jobstat_backend
```
cd jobstat_backend
```

Cria um virtualenv para a instalação da dependencias:
```
virtualenv jobstat
source jobstat/bin/activate
```

Instale as dependencias:
```
pip install -r requirements.txt
```

Executar os crawlers
```
cd crawlers
python apinfo_page_crawler.py
python ceviu_crawler.py
python netcarreiras_crawler.py
python trampos_api_crawler.py	
```
Os dados raspados serão salvos na pasta: crawled_data

Executar os normalizers
```
cd normalizers
python apinfoParser.py
python ceviuParser.py
python netcarreirasParser.py
python trampos_jsonParser.py
```
Os dados normalizadas serão salvos na pasta: normalized_data

Executar os analyzers
```
cd analyzers
python job_offer_counter.py
python skill_analyzer.py	
```
Os resultados serão salvos na pasta: analyzed_data


## Passo a Passo FrontEnd

Entra no arquivo jobstat_frontend
```
cd jobstat_frontend
```

Baixe as dependencias
```
npm install --save-dev gulp
bower install
```


Executa o projeto
```
gulp dev
```


## Grupo
Ryan David O'Mullan