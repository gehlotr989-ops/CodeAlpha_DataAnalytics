import pandas as pd

# CSV फाइल से डेटा लोड करना (सुनिश्चित करें कि scraped_quotes.csv उसी फोल्डर में है)
df = pd.read_csv('scraped_quotes.csv')

print("=== 1. डेटा का पहला हिस्सा (Head) ===")
print(df.head())

print("\n=== 2. डेटा की संरचना और डेटा टाइप्स (Info) ===")
print(df.info())

print("\n=== 3. सांख्यिकीय सारांश (Statistical Summary) ===")
print(df.describe())

print("\n=== 4. चेक करना कि क्या कोई वैल्यू मिसिंग (Missing) है ===")
print(df.isnull().sum())

print("\n=== 5. कुल यूनिक ऑथर्स (Unique Authors की संख्या) ===")
print(df['Author'].nunique())