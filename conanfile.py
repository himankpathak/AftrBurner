import shutil
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.files import get
from conan.tools.scm import Git
from conan.tools.microsoft import MSBuild


def report(status):
    print("########################################")
    print(f">>>>>    {status}    <<<<<")
    print("########################################")


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
    # Prevents unnecessary copy step
    no_copy_source = True

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

        report("Source fetched")

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(
            self, generator="Visual Studio 17 2022", build_folder="C:/repos_new/"
        )

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        try:
            if self.settings.os == "Windows":
                print(">> Copying to C:/repos")
                shutil.copytree(
                    self.export_sources_folder, "C:/repos_new/", dirs_exist_ok=True
                )
            else:
                print(">> Copying to ~/repos")
                shutil.copytree(self.export_sources_folder, "~/repos")
        except:
            print("Error copying build files")

        # cmake = CMake(self)
        # cmake.configure(
        #     cli_args=[
        #         "-A x64",
        #         "-S ./aburn/engine/src/aftr",
        #         "-B ./aburn/engine/cwin64",
        #     ]
        # )
        # cmake.build(target="INSTALL")
        self.run(
            'cmake -G "Visual Studio 17 2022" -A x64 -S ./aburn/engine/src/aftr -B ./aburn/engine/cwin64'
        )
        self.run(
            f"cmake --build ./aburn/engine/cwin64 --target INSTALL --config {self.settings.build_type}"
        )

        # msbuild = MSBuild(self)
        # msbuild.build_type = "Debug"
        # msbuild.platform = "x64"
        # msbuild.build("./aburn/engine/cwin64/AftrBurnerEngine.sln")
        # msbuild.build("./aburn/engine/cwin64/INSTALL.vcxproj")

        report("Build Finished")

    def package(self):
        pass
        # cmake = CMake(self)
        # cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["aftrburner"]
