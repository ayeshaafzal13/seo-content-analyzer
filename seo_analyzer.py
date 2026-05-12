# SEO CONTENT ANALYZER
# This script analyzes your article and prints a report

# STEP 1: Read the article from the text file
print("📖 Reading your article...")
try:
    with open("article.txt", "r", encoding="utf-8") as file:
        article_text = file.read()
    print("✅ Article loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: article.txt not found!")
    print("Make sure the file is in the same folder as this script.")
    exit()

# STEP 2: Count total words
# Split by spaces and punctuation, but for simplicity we'll split by spaces
words = article_text.split()
word_count = len(words)

# STEP 3: Count total sentences
# Count how many times we see . ! or ?
sentence_count = article_text.count('.') + article_text.count('!') + article_text.count('?')

# STEP 4: Keyword checker
# List of keywords to look for (convert everything to lowercase for accurate checking)
keywords = ["sialkot", "quality", "craftsmanship", "apex connect", "pakistan", "sportswear"]

# Create a results dictionary
keyword_results = {}
article_lower = article_text.lower()

for keyword in keywords:
    if keyword in article_lower:
        count = article_lower.count(keyword)
        keyword_results[keyword] = {"found": True, "count": count}
    else:
        keyword_results[keyword] = {"found": False, "count": 0}

# STEP 5: Print final summary report
print("=" * 55)
print("        SEO CONTENT ANALYSIS REPORT")
print("=" * 55)
print()

print("📊 BASIC STATISTICS:")
print(f"   • Total words: {word_count}")
print(f"   • Total sentences: {sentence_count}")
print(f"   • Average words per sentence: {word_count / sentence_count:.1f}")
print()

print("🔑 KEYWORD CHECKER:")
for keyword, result in keyword_results.items():
    status = "✅ FOUND" if result["found"] else "❌ NOT FOUND"
    print(f"   • '{keyword.title()}': {status} (appears {result['count']} time(s))")
print()

print("📈 SEO READINESS SCORE:")
# Simple scoring logic
found_keywords = sum(1 for r in keyword_results.values() if r["found"])
score = (found_keywords / len(keywords)) * 100
print(f"   • Keyword coverage: {found_keywords}/{len(keywords)} ({score:.0f}%)")
print()

if word_count >= 350 and word_count <= 450:
    print("✅ Word count is IDEAL (350-450 words)")
elif word_count < 350:
    print("⚠️  Word count is LOW (need at least 350 words)")
else:
    print("⚠️  Word count is HIGH (over 450 words is too long)")

print()
print("=" * 55)
print("              END OF REPORT")
print("=" * 55)