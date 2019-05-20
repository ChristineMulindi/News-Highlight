from flask import render_template, request, redirect
from . import main
from ..request import get_sources, get_source
from ..models import Articles

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    # Getting source
    general = get_sources('general')
    
    title = 'News-Highlight'
    
    return render_template('index.html', title=title, general=general)


@main.route('/source/<id>')
def articles(id):
    '''
    View source page function that returns the source details page and its data
    '''

    articles  = get_source(id)
    title = f'News -- {id}'
    id_articles = id
    # print(articles)
    return render_template('source.html', articles = articles)


