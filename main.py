import collections

def categorize_transaction(description: str) -> str:
    """
    Simulates an AI model categorizing a transaction description.
    In a real-world scenario, this would involve an API call to an LLM like Gemma 4.
    """
    description_lower = description.lower()

    # --- This is where an actual AI model (e.g., Gemma 4) would be invoked ---
    # Example: response = gemma_api.categorize(description)
    # For this example, we use simple keyword matching to simulate AI logic.
    if any(keyword in description_lower for keyword in ['starbucks', 'kahve', 'cafe', 'coffee']):
        return 'Coffee & Dining'
    elif any(keyword in description_lower for keyword in ['migros', 'carrefour', 'market', 'groceries']):
        return 'Groceries'
    elif any(keyword in description_lower for keyword in ['netflix', 'spotify', 'amazon prime', 'abonelik']):
        return 'Subscriptions'
    elif any(keyword in description_lower for keyword in ['uber', 'taksi', 'otobüs', 'transport']):
        return 'Transportation'
    elif any(keyword in description_lower for keyword in ['eczane', 'pharmacy', 'hastane', 'doktor']):
        return 'Health'
    elif any(keyword in description_lower for keyword in ['giyim', 'zara', 'hm', 'clothing']):
        return 'Apparel'
    elif any(keyword in description_lower for keyword in ['elektrik', 'su', 'internet', 'fatura']):
        return 'Utilities'
    elif any(keyword in description_lower for keyword in ['kira', 'rent']):
        return 'Housing'
    elif any(keyword in description_lower for keyword in ['sinema', 'konser', 'eğlence', 'entertainment']):
        return 'Entertainment'
    else:
        return 'Miscellaneous'
    # -----------------------------------------------------------------------


def main():
    # Sample credit card transactions (simulated input data)
    transactions = [
        {"description": "Starbucks Coffee", "amount": 120.50},
        {"description": "Migros Supermarket", "amount": 450.75},
        {"description": "Netflix Subscription", "amount": 99.99},
        {"description": "Uber Ride", "amount": 85.00},
        {"description": "Local Pharmacy", "amount": 60.20},
        {"description": "Zara Clothing", "amount": 320.00},
        {"description": "Carrefour Market", "amount": 210.30},
        {"description": "Spotify Premium", "amount": 49.99},
        {"description": "Electricity Bill", "amount": 180.00},
        {"description": "Cinema Tickets", "amount": 150.00},
        {"description": "Local Cafe", "amount": 75.00}
    ]

    categorized_spending = collections.defaultdict(float)
    print("--- AI-Powered Transaction Categorization ---")
    print("\nOriginal Transaction -> Categorized As")
    print("----------------------------------------")

    for i, transaction in enumerate(transactions):
        description = transaction["description"]
        amount = transaction["amount"]
        
        # Use the simulated AI to categorize the transaction
        category = categorize_transaction(description)
        
        print(f"'{description}' (₺{amount:.2f}) -> {category}")
        categorized_spending[category] += amount

    print("\n--- Spending Summary by Category ---")
    print("----------------------------------")
    for category, total_amount in sorted(categorized_spending.items()):
        print(f"{category}: ₺{total_amount:.2f}")
    print("----------------------------------")
    print(f"Total Spending: ₺{sum(categorized_spending.values()):.2f}")

if __name__ == "__main__":
    main()
