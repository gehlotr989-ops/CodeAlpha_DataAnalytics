import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV फाइल लोड करना
df = pd.read_csv('scraped_quotes.csv')

# विजुअलाइजेशन के लिए स्टाइल सेट करना
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# ऑथर्स के कोट्स की संख्या का बार चार्ट बनाना
author_counts = df['Author'].value_counts().head(5)
sns.barplot(x=author_counts.values, y=author_counts.index, palette='crest')

# चार्ट के शीर्षक और लेबेल
plt.title('Top Authors by Quote Count', fontsize=14, fontweight='bold')
plt.xlabel('Number of Quotes', fontsize=12)
plt.ylabel('Author', fontsize=12)

plt.tight_layout()

# चार्ट को इमेज के रूप में सेव करना
plt.savefig('task3_author_visualization.png')
print("डेटा विजुअलाइजेशन चार्ट 'task3_author_visualization.png' के रूप में सफलताપूर्वक सेव हो गया है!")

# चार्ट स्क्रीन पर दिखाने के लिए
plt.show()