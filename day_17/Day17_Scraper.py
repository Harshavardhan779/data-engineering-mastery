from bs4 import BeautifulSoup
import pandas as pd

# 1. THE SOURCE: Create a dummy HTML file (Simulating a website)
html_content = """
<html>
    <head><title>Tech Store</title></head>
    <body>
        <h1>Featured Products</h1>
        <div class="product">
            <h2 class="name">Gaming Laptop</h2>
            <p class="price">$1200</p>
            <span class="status">In Stock</span>
        </div>
        <div class="product">
            <h2 class="name">Wireless Mouse</h2>
            <p class="price">$50</p>
            <span class="status">Out of Stock</span>
        </div>
        <div class="product">
            <h2 class="name">Mechanical Keyboard</h2>
            <p class="price">$150</p>
            <span class="status">In Stock</span>
        </div>
    </body>
</html>
"""

# Save this to a file so we can "scrape" it
with open("store.html", "w") as f:
    f.write(html_content)

print("🌐 'store.html' created. Starting Scraper...")

# 2. THE SCRAPER: Parse the HTML
with open("store.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

# Find all div elements with class "product"
products = soup.find_all("div", class_="product")

data = []

print(f"\n🕷️ Found {len(products)} products. Extracting details...")

for item in products:
    # Extract text from specific tags
    name = item.find("h2", class_="name").text
    price = item.find("p", class_="price").text
    status = item.find("span", class_="status").text
    
    # Clean the data (Remove '$')
    price_value = float(price.replace("$", ""))
    
    data.append({"Product": name, "Price": price_value, "Status": status})

# 3. SAVE: Export to CSV
df = pd.DataFrame(data)
print("\n📊 Scraped Data:")
print(df)

df.to_csv("scraped_products.csv", index=False)
print("\n✅ Data saved to 'scraped_products.csv'")