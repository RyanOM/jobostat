"""
    List of skills that will be analyzed in the skill_analyzer.py script
"""


# skill -> [subskill, subskill, ....]
SKILLS = {
    'java': [
        'spring',
        'hibernate',
        'jsf',
        'jboss',
        'jee'
    ],
    'javascript': [
        'angularjs',
        'nodejs',
        'emberjs',
        'backbonejs',
        'reactjs',
        'd3js',
        'jquery',
        'coffeescript',
        'vuejs',
        'typescript',
        'highcharts'
    ],
    'cobol': [],
    'c++': [],
    '.net': [
        'c#',
        'vb',
        'asp'
    ],
    'python': [
        'django',
        'flask',
        'web2py',
        'plone',
        'bottle',
        'scrapy'
    ],
    'ruby': [
        'rails',
        'sinatra'
    ],
    'sql': [
        'postgres',
        'mysql'
    ],
    'dba': [],
    'mongodb': [],
    'cassandra': [],
    'firebase': [],
    'mariadb': [],
    'cloud computing': [
        'aws',
        'azure',
        'heroku',
        'bluemix'
    ],
    'big data': [
        'hadoop',
        'spark',
        'hive'
    ],
    'perl': [],
    'scala': [
        'spark',
        'play framework',
        'akka'
    ],
    'clojure': [],
    'delphi': ['pascal'],
    'android': [],
    'ios': ['swift'],
    'mobile': [
        'ionic',
        'phonegap',
        'cordova',
        'android',
        'ios'
    ],
    'linux': [
        'ubuntu',
        'debian',
        'redhat'
    ],
    'php': [
        'wordpress',
        'magento',
        'drupal',
        'symfony',
        'cakephp',
        'symfony',
        'codeigniter',
        'zend',
        'joomla'
    ],
    'oracle': ['plsql'],
    'analytics': [
        'adwords',
        'seo',
        'sem',
        'excel'
    ],
    'design': [
        'photoshop',
        'illustrator',
        'indesign',
        'sketch',
        'flash',
        'invision',
        'marvel',
        'html5'
    ],
    'ibm': [
        'db2',
        'websphere'
    ],
    'agile': [
        'scrum',
        'tdd',
        'kanban'
    ],
    'erlang': [],
    'go': [],
    'rust': [],
    'haskell': [],
    'lua': [],
    'matlab': [],
    'r': [],
    'groovy': ['grails'],
    'lisp': [],
    'fortran': [],
    'unity': [],
    'jenkins': [],
    'ansible': [],
    'docker': []

}

# Find skills that have multiple used names rails -> ruby on rails
ALIASES = {
    'ruby on rails': 'rails',
    'mongo': 'mongodb',
    'angular.js': 'angularjs',
    'angular': 'angularjs',
    'node': 'nodejs',
    'node.js': 'nodejs',
    'ember.js': 'emberjs',
    'backbone.js': 'backbonejs',
    'react.js': 'reactjs',
    'd3.js': 'dsjs',
    'vue.js': 'vuejs',
    'dotnet': '.net',
    'java script': 'javascript',
    'postgres': 'postgresql',
    'golang': 'go',
    'delphi': 'delphi7'
}
