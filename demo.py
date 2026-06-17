def convert_method_name(method_name):
    """Convert camelCase method names (starting with 'get') to snake_case format.
    
    Examples:
        getCurrency -> Currency
        getAccountName -> Account_Name
        getLongAccountName -> Long_Account_Name
        getTradeID -> Trade_ID
        getSWIFTCode -> SWIFT_Code
    """
    # Remove 'get' prefix
    if method_name.startswith('get'):
        name = method_name[3:]
    else:
        name = method_name
    
    result = []
    for i, char in enumerate(name):
        if char.isupper():
            # Insert underscore before uppercase letter if:
            # 1. Previous character is lowercase, OR
            # 2. Previous is uppercase AND next is lowercase (transition from acronym to word)
            if i > 0:
                prev_char = name[i-1]
                next_char = name[i+1] if i+1 < len(name) else None
                
                if prev_char.islower():
                    # Previous char is lowercase
                    result.append('_')
                elif prev_char.isupper() and next_char and next_char.islower():
                    # Transition from acronym to regular word
                    result.append('_')
        
        result.append(char)
    
    return ''.join(result)


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("getCurrency", "Currency"),
        ("getAccountName", "Account_Name"),
        ("getLongAccountName", "Long_Account_Name"),
        ("getTradeID", "Trade_ID"),
        ("getSWIFTCode", "SWIFT_Code"),
    ]
    
    for input_str, expected in test_cases:
        result = convert_method_name(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} {input_str} -> {result} (expected: {expected})")