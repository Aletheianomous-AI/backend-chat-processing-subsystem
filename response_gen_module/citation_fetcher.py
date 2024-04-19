from duckduckgo_search import DDGS as searcher
from duckduckgo_search.exceptions import DuckDuckGoSearchException as ddgse

class Citation_Fetcher():

    def parse_results(raw_results):
        results_output = ""
        i = 1
        for item in raw_results:
            results_output += "["  + str(i) + "] "
            results_output += item['href'] + " : "
            results_output += item['body'] + "\n"
            i+=1
        return results_output
    
    def search_online(query):
        raw_results = None
        try:
            search_instance = searcher()
            raw_results = search_instance.text(query, max_results=3)
            parsed_results = self.parse_results(raw_results)
        except ddgse:
            raise ddgse()
        return raw_results, parsed_results
