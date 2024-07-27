from conan import ConanFile

class SystemShockRecipe(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  generators = "CMakeToolchain", "CMakeDeps"

  def requirements(self):
    #self.requires("fluidsynth/2.3.5") # Not yet in Conan Center, see
    #                                  # <https://github.com/conan-io/conan-center-index/issues/15397>
    if self.settings.os != "Windows":
      self.requires("libalsa/1.2.10")
    self.requires("opengl/system")
    self.requires("sdl/2.28.5") # sdl_mixer/2.8.0 currently conflicts with sdl/2.30.5
    self.requires("sdl_mixer/2.8.0")
