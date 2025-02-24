# Fraktal Technical Challenge - Option 2: Virtual Filesystem Challenge
Used Python version: 3.12

## Usage
#### CLI
Cli interface of the VFS can be installed by cloning the repository and running `pip install .` inside the project directory.

Interface can be started by calling `mount`.

Interface mimics basic unix commands for file operations, which can be seen below. You can use command `test_env` to create a test environment quickly. 

Command completion works on selected commands (cd, touch) and you can traverse command history with up and down arrows.

#### API

API has been developed largely taking CLI interface requirements into consideration.
API can be used as an external library through installing the Github repository via pip or adding it to dependencies as a module.

Example (setuptools needed):

``pip install git+https://github.com/juusosar/virtual_filesystem.git@master``

You get access to the API commands by introducing the ``src.core.MyVFS()`` object.

Unfortunately I didn't have time to test this properly (as with quite many other things).


### Table for commands and API equivalents

| CLI Command       	 | API Command             	                                |
|---------------------|----------------------------------------------------------|
| cd                	 | change_active_directory 	                                |
| ls                	 | list_current_directory  	                                |
| mkdir             	 | create_directory        	                                |
| pwd               	 | print_current_directory 	                                |
| rm                	 | delete_file             	                                |
| cat               	 | read_file               	                                |
| cat [-w\|-w+\|-a] 	 | write_file              	                                |
| touch             	 | create_file             	                                |
| find           	    | find_directory, find_file(Not implemented)             	 |
| 	                   | file_exists             	                                |
| 	                   | list_directories            	                            |
| 	                   | list_directories_and_files           	                   |
| 	                   | reset           	                                        |
| cp 	                | copy_file (Not implemented)                              |
| mv                  | move_file (Not implemented)            	                 |
| rmdir             	 | delete_directory (Not implemented)                       |

## Data structures
I decided on a hybrid approach after evaluating the use cases of both tree structure and a hashmap structure. 

The folder structure of the filesystem follows a tree structure with each directory having their parent and child directories
as attributes for simple and efficient directory traversal and directory listing. The root directory is situated in "/".

The file structuring inside the directories on the other hand is implemented by a hashmap in the form of a dictionary,
with the file names as keys and the file contents as values.

Directories can be traversed recursively since they have references to their subdirectories and their parent directory.

I wanted to use only built-in libraries as much as I can to keep the project lightweight on dependencies.
External library usage: ``setuptools`` and ``pyreadline3``. ``setuptools`` for easily installing the project, 
``pyreadline3`` for command completion and command history functionality for the interface.

## Limitations and areas for improvement
Time constraints were the biggest hurdle for me while doing this challenge.

Python is not the most efficient language to do this challenge in
but in my case it was the language of choice since it is the one I am the most proficient in.

Regarding performance, I didn't have the opportunity to test the filesystem functionality in large sets of objects.
There are certainly performance upgrades I could implement to the directory traversal algorithm

The filesystem does not work in tandem with or can't mock an actual filesystem (á la pyfakefs).

I also planned on implementing atomic operations or locks for threading use and especially for vital operations such as reading and writing files.

Files are represented only as plain strings, I planned originally on using byte stream IO for the files but needed to cut the functionality.


## Future 
Finishing the missing API commands and adding them to the interface.

Implementing the planned search algorithm for searching files in the filesystem.

- redis or memcached for persistent data between sessions without writing to disk
- data only in strings - byte stream and more complex data types
- Different filetypes (own inherited classes) based on content type
- Automated testing pipeline with more thorough tests

### Disclosing AI use
A friendly neighbourhood LLM consulted with following:
- Creating regex for checking valid paths
- Inspiration for directory traversal loop
- Working as a Google-on-steroids option on some topics