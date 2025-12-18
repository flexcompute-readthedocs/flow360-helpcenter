#!/usr/bin/env python3
"""
Script to remove {toctree} sections from all Markdown files in the docs folder.
This script recursively searches for .md files and removes any MyST toctree directives.
It can also remove MyST "target" labels used for stable references, e.g. `(my-label)=`.
"""

import os
import re
import glob
from pathlib import Path
import argparse

def remove_toctree_sections(content):
    """
    Remove {toctree} sections from markdown content.
    
    Args:
        content (str): The markdown content to process
        
    Returns:
        str: Content with toctree sections removed
    """
    # Pattern to match {toctree} sections with newlines
    # Matches: ```{toctree}\n...\n```
    toctree_pattern = r'```\{toctree\}.*?```'
    
    # Remove all toctree sections
    cleaned_content = re.sub(toctree_pattern, '', content, flags=re.DOTALL)

    # Pattern to match MyST target labels used for stable references.
    # Matches lines like: (reference)=
    # See: https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html
    target_label_pattern = r'(?m)^[ \t]*\([A-Za-z0-9_.:-]+\)=\s*(?:\r?\n)?'

    # Remove all target-label lines
    cleaned_content = re.sub(target_label_pattern, '', cleaned_content)
    
    return cleaned_content


def remove_myst_refs(content):
    """
    Remove MyST target labels used for stable references, e.g. `(my-label)=`.
    """
    target_label_pattern = r'(?m)^[ \t]*\([A-Za-z0-9_.:-]+\)=\s*(?:\r?\n)?'
    return re.sub(target_label_pattern, '', content)

def process_markdown_files(docs_folder):
    """
    Process all .md files in the docs folder and remove toctree sections.
    
    Args:
        docs_folder (str): Path to the docs folder
    """
    docs_path = Path(docs_folder)
    
    if not docs_path.exists():
        print(f"Error: Docs folder '{docs_folder}' does not exist.")
        return
    
    # Find all .md files recursively
    md_files = list(docs_path.rglob("*.md"))
    
    if not md_files:
        print(f"No .md files found in '{docs_folder}'")
        return
    
    print(f"Found {len(md_files)} .md files to process...")
    
    processed_count = 0
    modified_count = 0
    
    for md_file in md_files:
        try:
            # Read the file content
            with open(md_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # Remove toctree sections
            cleaned_content = remove_toctree_sections(original_content)
            
            # Check if content was modified
            if cleaned_content != original_content:
                # Write the cleaned content back to the file
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                modified_count += 1
                print(f"Modified: {md_file}")
            else:
                print(f"No changes needed: {md_file}")
            
            processed_count += 1
            
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
    
    print(f"\nProcessing complete!")
    print(f"Total files processed: {processed_count}")
    print(f"Files modified: {modified_count}")

def main():
    """Main function to run the script."""
    # Get the current script's directory and navigate to the docs folder
    parser = argparse.ArgumentParser(
        description="Remove myst-parser specific toctree sections from md files in a directory."
    )

    parser.add_argument("dir", help="Directory to be processed", type=str)

    args = parser.parse_args()

    docs_folder = args.dir
    

    process_markdown_files(docs_folder)


if __name__ == "__main__":
    main()
