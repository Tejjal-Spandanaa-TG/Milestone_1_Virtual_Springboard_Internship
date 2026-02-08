import pandas as pd
CATEGORIES = {
    "Delivery": [
        "delivery", "shipped", "arrived", "late", "delayed", "fast delivery",
        "shipping", "package", "received", "time", "quick", "slow delivery"
    ],
    "Product": [
        "product", "quality", "excellent", "worst", "good", "bad", "poor",
        "defective", "broken", "item", "material", "design", "features"
    ],
    "Support": [
        "support", "help", "customer support", "team", "helpful", "respond",
        "response", "assistance", "service", "complaint", "issue", "problem"
    ],
    "Price": [
        "price", "cost", "expensive", "cheap", "money", "waste", "affordable",
        "discount", "value", "paid", "worth"
    ]
}
def classify_feedback(feedback):
    feedback_lower = str(feedback).lower()
    category_scores = {}   
    for category, keywords in CATEGORIES.items():
        score = 0
        for keyword in keywords:
            if keyword in feedback_lower:
                score += 1
        category_scores[category] = score
    max_score = max(category_scores.values())
    if max_score == 0:
        return "General"
    for category, score in category_scores.items():
        if score == max_score:
            return category    
    return "General"
def main():
    file_path = "Milestone1_Cleaned_Feedback.csv"    
    try:
        df = pd.read_csv(file_path)
        print("Successfully loaded cleaned feedback data.")
        print(f"Total feedbacks: {len(df)}\n")
    except FileNotFoundError:
        raise ValueError(f"❌ File '{file_path}' not found.")    
    if "clean_feedback" not in df.columns:
        raise ValueError("❌ 'clean_feedback' column not found in CSV file")
    df["category"] = df["clean_feedback"].apply(classify_feedback)
    print(df[["feedback", "clean_feedback", "category"]].head(20))
    print("\n")
    print("CATEGORY DISTRIBUTION")
    category_counts = df["category"].value_counts()
    for category, count in category_counts.items():
        percentage = (count / len(df)) * 100
        print(f"{category:15} : {count:4} feedbacks ({percentage:6.2f}%)")
    print("\n")
    output_file = "Classified_Feedback.csv"
    df.to_csv(output_file, index=False)
    print(f"Classification completed successfully")
    print(f"Results saved to '{output_file}'")
    print("\n")
    print("DETAILED FEEDBACK WITH CATEGORIES")
    for idx, row in df.head(30).iterrows():
        print(f"\n[ID {row['feedback_id']}] Category: {row['category']}")
        print(f"Original: {row['feedback']}")
        print(f"Cleaned:  {row['clean_feedback']}")        
if __name__ == "__main__":
    main()

