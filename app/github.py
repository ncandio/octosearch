import requests
from app.config import Config

class GitHubAPI:
    BASE_URL = 'https://api.github.com'
    
    @staticmethod
    def search_repositories(query, sort='stars', order='desc'):
        """
        Search for repositories on GitHub.
        
        Args:
            query (str): The search query
            sort (str): The sort field, e.g., 'stars', 'forks', 'updated'
            order (str): The sort order, either 'asc' or 'desc'
            
        Returns:
            dict: The JSON response from the GitHub API
        """
        headers = {}
        if Config.GITHUB_TOKEN:
            headers['Authorization'] = f'token {Config.GITHUB_TOKEN}'
        
        url = f'{GitHubAPI.BASE_URL}/search/repositories'
        params = {
            'q': query,
            'sort': sort,
            'order': order
        }
        
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    
    @staticmethod
    def search_code(query, sort='best-match', order='desc', per_page=30, page=1):
        """
        Search for code on GitHub.
        
        Args:
            query (str): The search query
            sort (str): The sort field, either 'best-match' or 'indexed'
            order (str): The sort order, either 'asc' or 'desc'
            per_page (int): Number of results per page (max 100)
            page (int): Page number for pagination
            
        Returns:
            dict: The JSON response from the GitHub API
        """
        headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        
        if Config.GITHUB_TOKEN:
            headers['Authorization'] = f'token {Config.GITHUB_TOKEN}'
        
        url = f'{GitHubAPI.BASE_URL}/search/code'
        params = {
            'q': query,
            'sort': sort,
            'order': order,
            'per_page': per_page,
            'page': page
        }
        
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
