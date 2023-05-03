from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get
from conan.tools.scm import Git
import shutil


class aftrburnerRecipe(ConanFile):
    name = "aftrburner"
    version = "1.0"

    # Optional metadata
    # license = "<Put the package license here>"
    # author = "<Put your name here> <And your email here>"
    # url = "<Package recipe repository url here, for issues about the package>"
    description = "A game design engine"
    topics = ("AftrBurner", "game", "engine")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    # exports_sources = "CMakeLists.txt", "src/*", "include/*"
    def source(self):
        # Faster but runs out daily traffic limit sooner on free plan
        # "https://dl.dropboxusercontent.com/s/ga8rvoccaqehu43/repo_distro.tar.xz",

        get(
            self,
            "https://catmailohio-my.sharepoint.com/:u:/g/personal/hp433822_ohio_edu/EbNegRqVgZZJgUsetTwLco0BZfvg8wONpiKNhd-r7xkj_g?download=1",
            strip_root=True,
            filename="repo_distro.tar.xz",
        )

        # For testing
        # self.run("xcopy Y:\\repo_distro2\\* . /E")

        self.run("dir")

        git = Git(self, folder="aburn/engine")
        git.checkout("-- *")

        git = Git(self, folder="libs")
        git.checkout("-f --")

        git = Git(self, folder="aburn/usr")
        git.checkout("-- *")

        git = Git(self, folder="aburn/modules")
        git.checkout("-- *")
        shutil.move("aburn/modules", "aburn/usr/modules")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["aftrburner"]
