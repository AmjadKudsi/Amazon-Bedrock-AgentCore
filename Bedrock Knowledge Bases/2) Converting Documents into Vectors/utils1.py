# complete the load_documents_from_folder() function in the provided code

import os
from pathlib import Path

def load_documents_from_folder(path):
    # TODO: Create an empty list to store loaded documents
    documents = []

    # TODO: Iterate through all files in the given folder path
    for filename in os.listdir(path):

        # TODO: For each item, construct the full file path
        filepath = Path(os.path.join(path, filename))

        # TODO: Check if the path is a file (not a directory)
        if filepath.is_file():

            # TODO: Try to open and read the file content (use utf-8 encoding)
            try:

                # TODO: If the content is not empty, create a document dictionary with:
                #   - "key": filename without extension
                #   - "content": file content
                #   - "metadata": dictionary with "filename"
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read().strip()

                # TODO: Append the document dictionary to your list
                if content:
                    documents.append({
                        "key": filepath.stem,
                        "content": content,
                        "metadata": {
                            "filename": filepath.name
                        }
                    })

            # TODO: Handle any exceptions that occur during file reading
            except Exception as e:
                print(f"Error loading {filepath.name}: {e}")

    # TODO: Return the list of loaded documents
    return documents