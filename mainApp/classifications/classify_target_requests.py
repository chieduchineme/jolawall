# classify_target_requests.py
import pandas as pd

def extract_labels(requests):
    # Short descriptions for each attack type
    descriptions = {
        "Content_Scraping": "Extracting large amounts of data from a website without authorization.",
        "Forced_Browsing_Attacks": "Accessing unintended resources by manipulating URLs or parameters.",
        "LdapInjection": "Injecting malicious LDAP queries into directory services.",
        "Local_File_Inclusion": "Including unauthorized local files on the server.",
        "Malicious_Downloads": "Delivering harmful files disguised as legitimate downloads.",
        "OsCommanding": "Injecting OS commands to execute unauthorized server actions.",
        "PathTransversal": "Manipulating file paths to access unauthorized files or directories.",
        "Remote_File_Inclusion": "Including remote files to execute malicious scripts.",
        "SSI": "Exploiting server-side include functionality for unauthorized commands.",
        "Script_Injection": "Injecting scripts to manipulate behavior or steal data.",
        "Sensitive_Data_Exposure": "Unauthorized access to sensitive information.",
        "SqlInjection": "Exploiting database vulnerabilities to manipulate or retrieve data.",
        "Unauthorized_Access": "Gaining unauthorized access to resources or systems.",
        "XPathInjection": "Injecting XPath queries to manipulate or access XML data.",
        "XSS": "Injecting malicious scripts into web pages viewed by others.",
        "Valid": "Refers to normal, non-malicious traffic."
    }

    features = []

    for req in requests:
        # Extract the class from the request
        req_class = req.get("class", "Unknown Type")
        category = "Valid" if req_class == "Valid" else "Malicious"

        # Handle multi-class attacks
        if isinstance(req_class, str) and "[" in req_class and "]" in req_class:
            # Parse multi-class list from string safely
            try:
                classes = eval(req_class)  # Converts string representation to Python list
            except (SyntaxError, ValueError):
                classes = ["Unknown Type"]  # Handle invalid format safely

            # Attach descriptions for multi-class
            description = "; ".join(f"{cls}-{descriptions.get(cls, 'Unknown attack type')}" for cls in classes)
        elif isinstance(req_class, list):
            # If req_class is already a list
            description = "; ".join(f"{cls}-{descriptions.get(cls, 'Unknown attack type')}" for cls in req_class)
        else:
            # Single class description
            description = descriptions.get(req_class, "Unknown attack type")

        # Add to features list
        feature = {
            "class": req_class,
            "category": category,
            "descriptionOfClass": description
        }
        features.append(feature)

    # Convert the list of features into a DataFrame
    return pd.DataFrame(features)


def extract_features2(requests):
    features = []

    for req in requests:
        feature = {
                "timestamp": req.get("timestamp"),
                "source": req.get("ip"),
                "original_url": req.get("original_url"),
                "user_agent": req.get("user_agent"),
                "method": req.get("method"),
                "query": req.get("query"),
                "cookies": req.get("cookies"),
                "asn": req.get("asn"),
                "blacklist": req.get("blacklist"),
                "headers": req.get("headers", {}).get("Authorization"),
                "body": req.get("body", {})
            }

        # Append the feature dictionary to the features list
        features.append(feature)

    # Convert the list of features into a DataFrame
    return pd.DataFrame(features)


def extract_dbFeatures(requests):
    features = []

    # Iterate over the rows of the DataFrame
    for index, row in requests.iterrows():
        # Convert the row to a dictionary (each row is a Pandas Series)
        req = row.to_dict()

        # Extract fields directly from the request dictionary
        feature = {
            "timestamp": req.get("timestamp"),
            "source": req.get("ip"),
            "original_url": req.get("original_url"),
            "user_agent": req.get("user_agent"),
            "method": req.get("method"),
            "query": req.get("query"),
            "cookies": req.get("cookies"),
            "asn": req.get("asn"),
            "blacklist": req.get("blacklist"),
            "headers": req.get("headers", {}),
            "body": req.get("body", {}),
        }

        # Append the feature dictionary to the features list
        features.append(feature)
    # Convert the list of features into a DataFrame
    return pd.DataFrame(features)
