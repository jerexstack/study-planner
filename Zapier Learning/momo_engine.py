def process_transaction(raw_reference):
    """ 
    Takes a human-typed reference string, cleans is, and returns a clean string along with its detected routing bucket
    """
    clean_text = raw_reference.strip().replace(".", "").upper()
    if "FEES" in clean_text:
        category = "TUTION ACCOUNT"
    elif "SCH" in clean_text:
        category = "TUTION ACCOUNT"
    else:
        category = "SUSPENSE ACCOUNT"
    return clean_text, category
    
if __name__ == "__main__":
    print("  [TEST MODE] Running engine directly...")
    test_text, test_cat = process_transaction("   s4  FeEs  ")
    print(f"Test Input Cleansed to: '{test_text}' and routed to: {test_cat}")
