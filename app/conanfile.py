from io import StringIO

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class appRecipe(ConanFile):
    name = "app"
    package_type = "application"
    requires = (
        "liba/[>=0, include_prerelease]",
        "libb/[>=0, include_prerelease]",
    )

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def set_version(self):
        stdout = StringIO()
        self.run("dunamai from git --style semver --bump", cwd=self.recipe_folder, stdout=stdout)
        self.version = stdout.getvalue().strip()

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.variables["APP_VERSION"] = self.version
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()
