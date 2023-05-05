# AftrBurner Conan Recipe

## Setup Instructions
- Install Pre-requisites:
    - Visual Studio 2022
    - Git
    - CMake
    - Python (Install for all users)

- Install Conan package manager with `pip install conan`.

- To install AftrBurner with Conan you need to fetch the conan recipe. There are two ways to go about doing that.

    1. ### Use recipe in this repo
        - Clone the repository
        - cd into the root folder and run `python init.py`.
    
    2. ### Fetch recipe from conan-server
        - Create a new conan remote listing for the server with `conan remote add <server_name> <server_url>`.
        - Login into the server with `conan remote login <server_name> <user_name>`. Enter password when asked for.
        - Install AftrBurner MinSizeRel config with `conan install --requires=aftrburner/1.0 --build=aftrburner/1.0 -r=<server_name> --settings=build_type=MinSizeRel`
        - Install AftrBurner Debug config with `conan install --requires=aftrburner/1.0 --build=aftrburner/1.0 -r=<server_name> --settings=build_type=Debug`

- AftrBurner is now installed in C:/repos or ~/repos directory.

### Hosting the package on custom conan server
- Install `conan-server` package with `pip install conan-server`
- Run `conan_server` to start the server for the first time.
- Modify $HOME/.conan_server/server.conf and restart the server.
    - Add `*/*@*/*: user` to [write_permissions]
    - Add `user: pass` to [users]
- After building the AftrBurner engine successfully once with the recipe cloned from the GitHub repository, it is ready to be hosted on our server.
- Add the server to the conan remote listing and login using the commands mentioned above.
- Push the recipe to the server with `conan upload aftrburner -r=<server_name> --only-recipe`
- AftrBurner recipe is now available to download from our custom conan server.


### Author
[Himank Pathak](https://github.com/himankpathak)