# Fraktal Technical Challenge - Option 2: Virtual Filesystem Challenge
Python version: 3.12

## Data structures
I decided on a hybrid approach after evaluating the use cases of both tree structure and a hashmap structure. 

The folder structure of the filesystem follows a tree structure with each directory having their parent and child directories
as attributes for simple and efficient directory traversal and directory listing. The root directory naturally doesn't have
a parent, and it is situated in "/".

The file structuring inside the directories on the other hand is implemented by a hashmap in the form of a dictionary,
with the file names as keys and th file contents as values.

## Challenges

## Notes
Python is not the most efficient language to do a VFS in
but in my case it was the easy choice since it is the language I am the most proficient in.

### Disclosing AI use
A friendly neighbourhood LLM consulted with following:
- Creating regex for checking valid paths
- Inspiration for directory traversal loop