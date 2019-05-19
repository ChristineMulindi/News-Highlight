from flask import render_template
from app import app
from request import get_sources
from request import get_source

# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting source
    sports = get_sources('sports')
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    business = get_sources('business')
    general = get_sources('general')


    title = 'Welcome to The best News Highlight'
    
    return render_template('index.html', title=title, technology=technology, sports=sports, entertainment=entertainment, business=business, general=general)


@app.route('/source')
def source():
    '''
    View source page function that returns the source details page and its data
    '''
    

    sports = get_sources('sports')
    print(sports)
    technology = get_sources('technology')
    entertainment = get_sources('entertainment')
    business = get_sources('business')
    general = get_sources('general')

    title = 'Welcome to The best News Highlight'

    return render_template('index.html', title=title, sports=sports, technology=technology, entertainment=entertainment, business=business, general=general)


@app.route('/source/articles')
def articles():
    '''
    View article page function that returns the article details page and its data
    '''

    sports = get_source('sports')
    technology = get_source('technology')
    entertainment = get_source('entertainment')
    business = get_source('business')
    general = get_source('general')

    title = 'Welcome to The best News Highlight'

    return render_template('articles.html', title=title, sports=sports, technology=technology, entertainment=entertainment, business=business, general=general)