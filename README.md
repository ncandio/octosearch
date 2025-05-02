# OctoSearch

![Screenshot 2025-05-02 030249](https://github.com/user-attachments/assets/683adb91-1c47-4d2a-8306-64eb831a478d)


A simple web application for searching code across GitHub repositories using the GitHub Search API. This project is a simple exercise for learning Flask, a micro web framework written in Python.

For more information about Flask, check out the official documentation at [https://flask.palletsprojects.com/en/stable/](https://flask.palletsprojects.com/en/stable/).

## Features

- Search code across GitHub repositories
- Filter results by organization, user, repository, language, and more
- Sort results by relevance or recently indexed
- Pagination for large result sets

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/octosearch.git
   cd octosearch
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   ```
   
   Then edit `.env` to add your GitHub personal access token for higher rate limits. Without a token, GitHub API imposes strict rate limits (10 requests per minute for unauthenticated users).

## Usage

1. Start the development server:
   ```
   python run.py
   ```

2. Open your web browser and go to http://127.0.0.1:5000

## GitHub API Token

To avoid rate limiting when using the application:

1. Create a GitHub personal access token:
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Generate a new token with the `public_repo` scope
   - Copy your token

2. Add the token to your `.env` file:
   ```
   GITHUB_TOKEN=your-token-here
   ```

3. Restart the application if it's already running

With an authenticated token, your rate limit increases to 30 requests per minute instead of 10 for unauthenticated requests.

## Search Syntax

OctoSearch supports GitHub's code search qualifiers:

- `keyword` - Search for code containing the keyword
- `org:organization` - Limit search to an organization
- `user:username` - Limit search to a user's repositories
- `repo:username/repo` - Limit search to a specific repository
- `language:name` - Limit search to a programming language
- `path:directory` - Limit search to file paths
- `extension:ext` - Limit search to file extensions
- `size:n` - Limit search to files of size n kilobytes
- `in:file,path` - Search in file contents and/or paths

## License

MIT License

## Acknowledgements

- This project uses the [GitHub Search API](https://docs.github.com/en/rest/search)
- Built with Flask, a lightweight WSGI web application framework
