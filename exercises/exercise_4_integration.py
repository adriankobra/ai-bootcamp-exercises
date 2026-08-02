"""
Exercise 4: Integration Challenge
===================================

Build a mini data pipeline that processes text documents.
This exercise has three levels — complete as far as you can.

- BASE: File reading and text processing (no LLM needed)
- STANDARD: Add LLM-based analysis
- ADVANCED: Production-grade pipeline with error recovery

Uses the same LLM provider configured in utils/llm_client.py.
"""

import json
from pathlib import Path
from collections import Counter

from utils import call_llm  # noqa: configured in utils/llm_client.py


DOCUMENTS_PATH = Path(__file__).parent.parent / "data" / "documents"
OUTPUT_PATH = Path(__file__).parent.parent / "output"


# ============================================================
# BASE LEVEL — File I/O and text processing (no LLM needed)
# ============================================================

def read_documents(folder: Path) -> list[dict]:
    """
    Read all .txt files from the given folder.
    Return a list of dicts: [{"filename": str, "content": str}, ...]
    """
    # TODO: Implement this function
    documents = []
    # https://www.geeksforgeeks.org/ need glob to choose only .txt
    for file in folder.glob("*.txt"):
        # read file 
        content = file.read_text(encoding="utf-8")
    #list of dicts
        documents.append({
            "filename": file.name,
            "content": content
        })
    #print (documents) check
    return documents





def word_count(text: str) -> int:
    """Return the number of words in a text."""
    # TODO: Implement this function
    #.split() to break it up by spaces
    words = text.split()

    return len(words)



def extract_keywords_simple(text: str, top_n: int = 5) -> list[str]:
    """
    Extract the top N most frequent meaningful words from text.
    Exclude common stop words (the, a, is, in, of, and, to, for, etc.)
    Return as a list of lowercase words.
    """
    # TODO: Implement without LLM — use word frequency
    # Exclude common stop words 
    stop_words = ["the", "a", "is", "in", "of", "and", "to", "for"]
    #lowercase and split 
    words = text.lower().split()
    filtered_words = []
    #for function where are no one stop words
    for word in words:
        # not the and etc.
        if word not in stop_words:
            filtered_words.append(word)
    #counts these words docs.python.org
    counts = Counter(filtered_words)
    
    ## return the most common words
    return [word for word, count in counts.most_common(top_n)]


def basic_stats(documents: list[dict]) -> dict:
    """
    Return basic statistics about the document set:
    - total_documents: int
    - total_words: int
    - avg_words_per_doc: float
    - shortest_doc: str (filename)
    - longest_doc: str (filename)
    """
    # TODO: Implement this function
    ## total_documents
    total_documents = len(documents)
    #total words in all documents
    total_words = 0

    # names of shortest and longest document
    shortest_doc = ""
    longest_doc = ""
    # number of words in shortest and longest document 100000 mean inf
    shortest_words = 1000000
    longest_words = 0
    #every document
    for doc in documents:

        #words in current document
        words = word_count(doc["content"])
        # add words to total
        total_words = total_words + words

        # if current document is shorter
        if words < shortest_words:
            shortest_words = words
            shortest_doc = doc["filename"]
        # if current document is longer
        if words > longest_words:
            longest_words = words
            longest_doc = doc["filename"]
    #avg  words
    avg_words_per_doc = total_words / total_documents
    # return statistics
    return {
        "total_documents": total_documents,
        "total_words": total_words,
        "avg_words_per_doc": avg_words_per_doc,
        "shortest_doc": shortest_doc,
        "longest_doc": longest_doc,
    }
# this part was difficult, so I used AI a little to understand the logic


# ============================================================
# STANDARD LEVEL — LLM-powered analysis
# ============================================================

def analyze_document(content: str) -> dict:
    """
    Use an LLM to analyze a single document and return:
    - summary: str (one sentence)
    - keywords: list[str] (3-5 keywords)
    - sentiment: str (positive/neutral/negative)
    """
    # TODO: Implement LLM-based analysis
    prompt = f"""
    Analyze the document:
    {content}

    return only:
    - summary: str (one sentence)
    - keywords: list[str] (3-5 keywords)
    - sentiment: str (positive/neutral/negative)
    
    Return ONLY valid JSON.
    Do not include explanations.
    Do not include markdown.
    
    """
    ## like 3 exercise
    response = call_llm(prompt)

    return json.loads(response)


def process_all_documents(documents: list[dict]) -> list[dict]:
    """
    Process all documents and return enriched results.
    Each result should contain: filename, summary, keywords, sentiment.
    """
    # TODO: Implement batch processing
    pass


def save_results(results: list[dict], output_path: Path) -> None:
    """Save results to a JSON file."""
    # TODO: Implement output saving
    pass


def generate_report(results: list[dict]) -> str:
    """
    Generate a formatted summary report containing:
    - Total documents processed
    - Sentiment distribution (how many positive/neutral/negative)
    - Top 10 most common keywords across all documents
    """
    # TODO: Implement report generation
    pass


# ============================================================
# ADVANCED LEVEL — Production-ready pipeline
# ============================================================

def process_with_recovery(documents: list[dict]) -> dict:
    """
    Process documents but handle failures gracefully:
    - If a document fails, log the error and continue
    - Retry failed documents once
    - Return both results and error log

    Return: {
        "results": [...],
        "errors": [{"filename": ..., "error": ...}],
        "success_rate": float
    }
    """
    # TODO: Implement fault-tolerant processing
    pass


def incremental_processing(documents: list[dict], output_path: Path) -> list[dict]:
    """
    Process documents incrementally:
    - Check if output file already exists
    - If yes, only process documents not already in the output
    - Append new results to existing output
    - This avoids re-processing and wasting API calls

    Return the complete results (existing + new).
    """
    # TODO: Implement incremental/resumable processing
    pass


def generate_comparison_report(results: list[dict]) -> str:
    """
    Generate an advanced report that also includes:
    - Document similarity (which documents cover similar topics?)
    - Topic clusters (group documents by dominant keyword overlap)
    - Confidence notes (which analyses might be unreliable and why?)
    """
    # TODO: Implement advanced reporting
    pass


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("  Exercise 4: Integration Challenge")
    print("=" * 60)

    # --- BASE ---
    print("\n--- BASE LEVEL ---")
    documents = read_documents(DOCUMENTS_PATH)
    if documents:
        print(f"Loaded {len(documents)} documents")
        stats = basic_stats(documents)
        if stats:
            print(f"Total words: {stats.get('total_words')}")
            print(f"Avg words/doc: {stats.get('avg_words_per_doc', 0):.0f}")
            print(f"Shortest: {stats.get('shortest_doc')}")
            print(f"Longest: {stats.get('longest_doc')}")

        # Show simple keyword extraction for first doc
        if documents:
            kw = extract_keywords_simple(documents[0]["content"])
            if kw:
                print(f"Keywords ({documents[0]['filename']}): {kw}")
    else:
        print("read_documents() not implemented yet")

    # --- STANDARD ---
    print("\n--- STANDARD LEVEL ---")
    if documents:
        results = process_all_documents(documents)
        if results:
            OUTPUT_PATH.mkdir(parents=True, exist_ok=True)
            save_results(results, OUTPUT_PATH / "analysis_results.json")
            print(f"Results saved to output/analysis_results.json")

            report = generate_report(results)
            if report:
                print(f"\n{report}")
        else:
            print("process_all_documents() not implemented yet")

    # --- ADVANCED ---
    print("\n--- ADVANCED LEVEL ---")
    if documents:
        recovered = process_with_recovery(documents)
        if recovered:
            print(f"Success rate: {recovered.get('success_rate', 0):.0%}")
            if recovered.get("errors"):
                print(f"Errors: {len(recovered['errors'])}")
        else:
            print("process_with_recovery() not implemented yet")
