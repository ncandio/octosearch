from flask import render_template, request, jsonify, redirect, url_for
from app.init import app
from app.github import GitHubAPI

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    if not query:
        return redirect(url_for('index'))
    
    sort = request.args.get('sort', 'best-match')
    order = request.args.get('order', 'desc')
    per_page = int(request.args.get('per_page', '30'))
    page = int(request.args.get('page', '1'))
    
    try:
        results = GitHubAPI.search_code(
            query=query,
            sort=sort,
            order=order,
            per_page=per_page,
            page=page
        )
        return render_template('results.html', query=query, results=results, request=request)
    except Exception as e:
        error_data = {
            'error': True,
            'message': str(e),
            'status_code': getattr(e, 'response', {}).get('status_code', 500)
        }
        return render_template('results.html', query=query, results=error_data, request=request)
