import requests
from typing import List, Dict
from config import WEB_SEARCH_API_KEY

class WebSearchAgent:
    def __init__(self, api_key=None):
        self.api_key = api_key or WEB_SEARCH_API_KEY

    def search(self, q: str, num: int = 5) -> List[Dict]:
        if not self.api_key:
            return [{
                'title': 'No-live-search-available',
                'snippet': 'WEB SEARCH API KEY not configured. Set WEB_SEARCH_API_KEY to enable live web results.',
                'url': None,
                'trust_score': 0.0
            }]
        return []