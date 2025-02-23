# Fraktal Technical Challenge - Option 2: Virtual Filesystem Challenge
Used Python version: 3.12

## Usage
CLI


API


### TODO: Table for commands and API equivalents

## Data structures
I decided on a hybrid approach after evaluating the use cases of both tree structure and a hashmap structure. 

The folder structure of the filesystem follows a tree structure with each directory having their parent and child directories
as attributes for simple and efficient directory traversal and directory listing. The root directory naturally doesn't have
a parent, and it is situated in "/".

The file structuring inside the directories on the other hand is implemented by a hashmap in the form of a dictionary,
with the file names as keys and the file contents as values.

Wanted to use only built-in libraries as much as I can to keep the project lightweight 

## Limitations
Python is not the most efficient language to do this challenge in
but in my case it was the language of choice since it is the one I am the most proficient in.

## Challenges

## Future 
- redis or memcached
- data only in strings - byte stream and more complex data types
- Automated testing pipeline with more thorough tests
- 

### Disclosing AI use
A friendly neighbourhood LLM consulted with following:
- Creating regex for checking valid paths
- Inspiration for directory traversal loop
- Working as a Google-on-steroids option on some topics