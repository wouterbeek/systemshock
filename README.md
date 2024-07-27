Shockolate - System Shock, but cross platform!
==============================================

Based on the source code for PowerPC released by Night Dive Studios, Incorporated.

[![Build Status TravisCI](https://travis-ci.org/Interrupt/systemshock.svg?branch=master)](https://travis-ci.org/Interrupt/systemshock) [![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/5fmcswq8n7ni0o9j/branch/master?svg=true)](https://ci.appveyor.com/project/Interrupt/systemshock)



GENERAL NOTES
=============

Shockolate is a cross platform source port of System Shock, using SDL2. This runs well on OSX, Linux, and Windows right now, with some missing features that need reviving due to not being included in the source code that was released.

The end goal for this project is something like what Chocolate Doom is for Doom: an experience that closely mimics the original, but portable and with some quality of life improvements including an OpenGL renderer and mod support!

Join our Discord to follow along with development: https://discord.gg/m45xPan

![work so far](https://i.imgur.com/kbVWQj4.gif)

Prerequisites
=============

- Original cd-rom or SS:EE assets in a `res/data` folder next to the executable
  - Floppy disk assets are an older version that we can't load currently



Running
=======

## Step 1: Install the prerequisites

1. Install CMake (e.g. `pip install -U cmake`).
2. Install Conan (e.g. `pip install -U conan`) and/or Vcpkg.
3. On Linux, install Ninja and GCC and/or Clang.
   On Windows, install Visual Studio.
4. From a purchased copy of System Shock, copy directory `RES/DATA`
   into directory `${projectDir}/res/data`.

## Step 2: Install the dependencies

```sh
cd ${projectDir}
```

2A. On POSIX with Conan:

```sh
conan install . -of build/posix/conan -b missing
```

2B. On POSIX with Vcpkg: nothing.

2C. On Windows with Conan:

```sh
conan install . -of build/windows/conan -b missing
```

2D. On Windows with Vcpkg: nothing.

## 3. Generate the build

3A. On POSIX with Conan:

```sh
cmake --preset posix-conan
```

3B. On POSIX with Vcpkg:

```sh
cmake --preset posix-vcpkg
```

3C. On Windows with Conan:

```sh
cmake --preset windows-conan
```

3D. On Windows with Vcpkg:

```sh
cmake --preset windows-pvckg
```

### Step 4: Build the binaries

4A. On POSIX with Conan:

```sh
cmake --build --preset posix-conan
```

4B. On POSIX with Vcpkg:

```sh
cmake --build --preset posix-vcpkg
```

4C. On Windows with Conan:

```sh
cmake --build --preset windows-conan
```

4D. On Windows with Vcpkg:

```sh
cmake --build --preset windows-vcpkg
```

### Step 5: Run the tools

5A. On POSIX with Conan:

```sh
./build/posix/conan/main
```

5B. On POSIX with Vcpkg:

```sh
./build/posix/vcpkg/main
```

5C. On Windows with Conan:

```
.\build\windows\conan\windows\tool\Release\main.exe
```

5D. On Windows with Vcpkg:

```
.\build\windows\vcpkg\windows\tool\Release\main.exe
```

### Step 6: Run the tests

6A: On POSIX with Conan:

```sh
ctest --preset posix-conan
```

6B: On POSIX with Vcpkg:

```sh
ctest --preset posix-vcpkg
```

6C. On Windows with Conan:

```sh
ctest --preset windows-conan
```

6D. On Windows with Vcpkg:

```sh
ctest --preset windows-vcpkg
```



Command line parameters
=======================

`-nosplash` Disables the splash screens, causes the game to start straight to the main menu

Modding Support
===============

Shockolate supports loading mods and full on fan missions. Just point the executable at a mod file or folder and the game will load it in. So far mod loading supports additional `.res` and `.dat` files for resources and missions respectively.

Run a fan mission from a folder:
```
./systemshock /Path/To/My/Mission
```

Run a fan mission from specific files:
```
./systemshock my-archive.dat my-strings.res
```



Control modifications
=====================

## Movement

Shockolate replaces the original game's movement with WASD controls, and uses `F` as the mouselook toggle hotkey. This differs from the Enhanced Edition's usage of `E` as the mouselook hotkey, but allows us to keep `Q` and `E` available for leaning.

## Additional hotkeys

* `Ctrl+G` cycles between graphics rendering modes
* `Ctrl+F` to enable full screen mode
* `Ctrl+D` to disable full screen mode 



Appendices
==========

## Appendix A: Install multiple compilers

On Ubuntu LTS, you can install one or more C/C++ compilers by running the following commands:

```sh
sudo apt install clang clang-18 gcc gcc-14 g++ g++-14
```

This is how the Ubuntu LTS versions compare to the latest versions (i.e. quite good):

| Compiler | Latest | Ubuntu 24.04 LTS |
| -------- | ------ | ---------------- |
| Clang    | 18.1.8 |           18.1.3 |
| GCC      | 14.1.0 |           14.0.1 |

It is easy to change your default compiler version on Ubuntu by using the `update-alternatives` tool. The following example installs 5 different versions of 2 different compilers. These are configures for the `update-alternatives` application by running `update-alternatives --install`. Finally, we configure which versions should be used when common compiler commands like `c++` and `cc` are used by running `update-alternatives --config`:

```sh
sudo apt install clang clang-17 clang-18
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-17 60 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-17
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-18 60 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-18
sudo update-alternatives --config clang

sudo apt install gcc gcc-13 gcc-14 g++ g++-13 g++-14
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 60 --slave /usr/bin/g++ g++ /usr/bin/g++-13
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-14 60 --slave /usr/bin/g++ g++ /usr/bin/g++-14
sudo update-alternatives --config gcc
```

The above commands were run on Ubuntu 24.04 LTS, but they will be very similar in other Ubuntu LTS releases.

### Conan profile compiler version

In case you use Conan to install the dependencies, make sure that your Conan profile only specifies the major version of your compiler, e.g. `compiler.version=14` and not `compiler.version=14.1`. It is easy to switch major compiler versions, but it is not easy to switch minor versions. (There is also no known use case for switching minor compiler versions in practice.)

### Clang Tools configuration

The same approach can be taken to install multiple versions of the Clang Tools.

#### Clang Check

```sh
sudo apt install clang-check-17 clang-check-18
sudo update-alternatives --install /usr/bin/clang-check clang-check /usr/bin/clang-check-17 60
sudo update-alternatives --install /usr/bin/clang-check clang-check /usr/bin/clang-check-18 60
sudo update-alternatives --config clang-check
```

#### Clang Format

`clang-format` is a tool which is built on top of LibFormat. We use this to format the C++ codebase. This is applied automatically for changed files on commit, if you have `clang-format` installed.

```sh
sudo apt install clang-format clang-format-17 clang-format-18
sudo update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-17 60
sudo update-alternatives --install /usr/bin/clang-format clang-format /usr/bin/clang-format-18 60
sudo update-alternatives --config clang-format
```

#### Clang Tidy

`clang-tidy` is a linter tool for C++. Installation is optional but will help you to identify problematic code and suggest improvements.

```sh
sudo apt install clang-tidy clang-tidy-17 clang-tidy-18
sudo update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-17 60
sudo update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-18 60
sudo update-alternatives --config clang-tidy
```
