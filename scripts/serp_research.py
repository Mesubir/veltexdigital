import json
import urllib.parse
import urllib.request
import sys
import os

SERP_API_KEY = "c0c30902efcb07962725b3122ada1b2ebd39015dbbc475e5cf4ad3d4e4dc7443"

def fetch_serp_data(query, location="India", num_results=10):
    params = {
        "engine": "google",
        "q": query,
        "location": location,
        "hl": "en",
        "gl": "in",
        "api_key": SERP_API_KEY,
        "num": num_results
    }
    url = "https://serpapi.com/search?" + urllib.parse.urlencode(params)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data
    except Exception as e:
        print(f"Error fetching SERP data: {e}")
        return None

def analyze_serp(query):
    print(f"=== Researching SERP for: '{query}' ===")
    data = fetch_serp_data(query)
    if not data:
        return
    
    results = {
        "query": query,
        "organic_results": [],
        "people_also_ask": [],
        "related_searches": []
    }
    
    if "organic_results" in data:
        for idx, res in enumerate(data["organic_results"][:10], 1):
            results["organic_results"].append({
                "position": idx,
                "title": res.get("title"),
                "link": res.get("link"),
                "snippet": res.get("snippet")
            })
            
    if "related_questions" in data:
        for q in data["related_questions"]:
            results["people_also_ask"].append(q.get("question"))
            
    if "related_searches" in data:
        for r in data["related_searches"]:
            results["related_searches"].append(r.get("query"))
            
    print(json.dumps(results, indent=2))
    return results

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "digital marketing agency for clinics in India"
    analyze_serp(query)
