from duckduckgo_search import DDGS as searcher
from duckduckgo_search.exceptions import DuckDuckGoSearchException as ddgse

class Citation_Fetcher():
    
    def search_online(query):
        raw_results = None
        try:
            search_instance = searcher()
            raw_results = search_instance.text(query, max_results=3)
        except ddgse:
            raise ddgse()
        return raw_results