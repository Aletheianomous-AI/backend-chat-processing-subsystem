from duckduckgo_search import DDGS as searcher

class Citation_Fetcher():
    def search_online(query):
        with searcher() as search_instance:
            raw_results = search_instance.text(query, max_results=10)
        return raw_results