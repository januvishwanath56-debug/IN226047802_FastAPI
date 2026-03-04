from fastapi import FastAPI

app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = []
    for p in products:
        if p["category"] == category_name:
            result.append(p)
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    instock = []
    for p in products:
        if p["in_stock"]:
            instock.append(p)
    return {"in_stock_products": instock, "count": len(instock)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    instock = 0
    categories = []

    for p in products:
        if p["in_stock"]:
            instock += 1
        if p["category"] not in categories:
            categories.append(p["category"])

    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": instock,
        "out_of_stock": total - instock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = []
    for p in products:
        if keyword.lower() in p["name"].lower():
            results.append(p)
    if not results:
        return {"message": "No products matched your search"}
    return {"results": results, "total_matches": len(results)}

@app.get("/products/deals")
def get_deals():
    cheapest = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])
    return {"best_deal": cheapest, "premium_pick": expensive}
