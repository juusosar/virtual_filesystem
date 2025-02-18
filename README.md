# Fraktal Technical Challenge - Option 2: Virtual Filesystem Challenge

## Data structures
I decided on a hybrid approach after evaluating the use cases of both tree structure and a hashmap structure. 

The folder structure of the filesystem follows a tree structure with each directory having their parent and child directories
as attributes for simple and efficient directory traversal and directory listing. The root directory naturally doesn't have
a parent, and it is situated in "/".

The file structuring inside the directories on the other hand is implemented by a hashmap in the form of a dictionary,
with the file names as keys and th file contents as values.

## Challenges