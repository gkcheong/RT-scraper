import re

def parseDocument(page):

    criticsScore = None
    audienceScore = None
    dateReleased = None
    genre = []
    director = []
    
    roughAudiencePattern = re.compile(r'href="#audience_reviews"[\s\w0-9\=\-\_\>\"\'\<\/]+%')
    roughCriticsPattern = re.compile(r'href="#contentReviews"[\s\w0-9\=\-\_\>\"\'\<\/]+%')
    roughDatePattern= re.compile(r'In Theaters: </div>\n<div class="meta-value">\n<time datetime="[0-9\-\w\:]+">[\s\w0-9\,]+</time>')
    roughDirectorPattern = re.compile(r'Directed By: </div>[\s\w0-9\=\-\_\>\"\'\<\/]+</div>')
    
    audiencePattern = re.compile(r'([0-9]+)\%')
    criticsPattern = re.compile(r'([0-9]+)\%')
    datePattern = re.compile(r'>([\s\w0-9\,]+)</time>')
    genrePattern = re.compile(r'<a href="/browse/opening/\?genres=[0-9]+">([\s\w\&\;]+)</a>')
    directorPattern = re.compile(r'<a href="/celebrity/[\w\_]+">([\s\w]+)</a>')
    #TODO:write method to clean genre and directors

    #search for audience score
    searchResult = re.search(roughAudiencePattern, page)
    if searchResult:
        searchResult = re.search(audiencePattern, searchResult.group(0))
        if searchResult:
            audienceScore = searchResult.group(1)
        
    #search for critics score
    searchResult = re.search(roughCriticsPattern, page)
    if searchResult:
        searchResult = re.search(criticsPattern, searchResult.group(0))
        if searchResult:
            criticsScore = searchResult.group(1)
        
    #search for date released
    searchResult = re.search(roughDatePattern, page)
    if searchResult:
        searchResult = re.search(datePattern, searchResult.group(0))
        if searchResult:
            dateReleased = searchResult.group(1)
            
    #search for genre
    genre = re.findall(genrePattern, page)
     
    #search for director
    searchResult = re.search(roughDirectorPattern, page)
    if searchResult:
        director = re.findall(directorPattern, searchResult.group(0))


    return [audienceScore, criticsScore, dateReleased, genre, director]