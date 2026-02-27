import os

def load_markdown_files(base_path = "knowledge"):
    documents = []

    for root, _, files in os.walk(base_path):
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                with open(full_path, "r", encoding = "utf-8") as f:
                    content = f.read()
                documents.append({
                    "content": content,
                    "source": full_path
                })
    return documents