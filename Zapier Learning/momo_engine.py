def process_transaction(raw_reference, amount):
    """
    Advanced Engine: Sanitizes raw input data streams and executes hierarchial routing logic with high vault tolorence.
    """

    if raw_reference is None:
        raw_reference = ""

    clean_text = raw_reference.strip().replace(".", "").upper()
    noisy_characters = [".", "#", "-", "/", "_", "(", ")"]

    for char in noisy_characters:
        clean_text = clean_text.replace(char, "")

    if amount >= 1000000:
        category = "VIP HIGH-VALUE ACCOUNT"

    elif "FEES" in clean_text or "SCH" in clean_text:
        category = "TUITION ACCOUNT"
    else:
        category = "SUSPENCE ACCOUNT"
    return clean_text, category

if __name__ == "__main__":
    print("Testing code laughing emoji's ")
    test1, cat1 = process_transaction("   s.4 fEes--  ", 1000000)
    print(f"Cleansed Sanitation: '{test1}' | Routing Target: '{cat1}' " )