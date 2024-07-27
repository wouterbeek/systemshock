cmake_minimum_required(VERSION 3.21)

project(shockolate VERSION 0.7.8)

include(FeatureSummary)

#set_property(GLOBAL PROPERTY FIND_LIBRARY_USE_LIB64_PATHS OFF)
#set_property(GLOBAL PROPERTY FIND_LIBRARY_USE_LIB32_PATHS ON)
set_property(GLOBAL PROPERTY FIND_LIBRARY_USE_LIB32_PATHS OFF)
set_property(GLOBAL PROPERTY FIND_LIBRARY_USE_LIB64_PATHS ON)

# Required for stdbool.h
set(CMAKE_C_STANDARD 99)
# For nullptr in C++
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g ")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -D__STDC_LIMIT_MACROS")

option(ENABLE_DEBUG_BLIT "Enable debugging blitter" OFF)
add_feature_info(ENABLE_DEBUG_BLIT ENABLE_DEBUG_BLIT "Enable debugging blitter")

# HAAAAX!!
add_definitions(-DSVGA_SUPPORT)

if(ENABLE_DEBUG_BLIT)
	add_definitions(-DDEBUGGING_BLIT)
endif()

add_compile_options(-fsigned-char -fno-strict-aliasing)

# ALSA
if(NOT WIN32)
	find_package(ALSA REQUIRED)
	add_definitions(-DUSE_ALSA)
endif(NOT WIN32)

# FluidSynth
find_package(FluidSynth)
if(FluidSynth_FOUND)
	add_definitions(-DUSE_FLUIDSYNTH)
endif(FluidSynth_FOUND)

# OpenGL
find_package(OpenGL REQUIRED)

# SDL 2
find_package(SDL2 REQUIRED)

# SDL 2 Mixer
find_package(SDL2_mixer REQUIRED)
add_definitions(-DUSE_SDL_MIXER=1)

# Generate version based on project version
set(PROJECT_REVERSION_STRING "")
find_package(Git)
if(GIT_FOUND)
	execute_process(COMMAND ${GIT_EXECUTABLE} describe --dirty
		WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
		OUTPUT_VARIABLE git_describe_out
		ERROR_VARIABLE git_describe_error
		RESULT_VARIABLE git_describe_result
		)
	string(REGEX MATCH "[a-z|0-9|.]*-[0-9]*-g([a-z|0-9]*)([-|a-z]*)" git_commit "${git_describe_out}")
	set(git_commit ${CMAKE_MATCH_1})
	set(git_dirty ${CMAKE_MATCH_2})
	set(PROJECT_REVERSION_STRING "-g${git_commit}${git_dirty}")
endif(GIT_FOUND)

message(STATUS "Version is ${PROJECT_VERSION}${PROJECT_REVERSION_STRING}")
configure_file("${CMAKE_SOURCE_DIR}/src/GameSrc/Headers/shockolate_version.h.in"
	"${CMAKE_BINARY_DIR}/src/GameSrc/Headers/shockolate_version.h" )

# Configuration done. Print features
feature_summary(WHAT ENABLED_FEATURES DESCRIPTION "Enabled features:")
feature_summary(WHAT DISABLED_FEATURES DESCRIPTION "Disabled features:")

# Sources configuration
add_subdirectory(src/Libraries/)

set(MAC_SRC
	src/MacSrc/ShockBitmap.c
	src/MacSrc/InitMac.c
	src/MacSrc/Shock.c
	src/MacSrc/Prefs.c
	src/MacSrc/MacTune.c
	src/MacSrc/SDLSound.c
	src/MacSrc/Modding.c
	src/MacSrc/OpenGL.cc
	src/MacSrc/Xmi.c
	src/MusicSrc/MusicDevice.c
)

set(GAME_SRC
	src/GameSrc/ai.c
	src/GameSrc/airupt.c
	src/GameSrc/amap.c
	src/GameSrc/amaploop.c
	src/GameSrc/ammomfd.c
	src/GameSrc/anim.c
	src/GameSrc/archiveformat.c
	src/GameSrc/audiolog.c
	src/GameSrc/automap.c
	src/GameSrc/bark.c
	src/GameSrc/biohelp.c
	src/GameSrc/cardmfd.c
	src/GameSrc/citres.c
	src/GameSrc/combat.c
	src/GameSrc/cone.c
	src/GameSrc/criterr.c
	src/GameSrc/cyber.c
	src/GameSrc/cybermfd.c
	src/GameSrc/cybmem.c
	src/GameSrc/cybrnd.c
	src/GameSrc/cutsloop.c
	src/GameSrc/damage.c
	src/GameSrc/digifx.c
	src/GameSrc/drugs.c
	src/GameSrc/effect.c
	src/GameSrc/email.c
	src/GameSrc/faceobj.c
	src/GameSrc/fixtrmfd.c
	src/GameSrc/frcamera.c
	src/GameSrc/frclip.c
	src/GameSrc/frcompil.c
	src/GameSrc/frmain.c
	src/GameSrc/frobj.c
	src/GameSrc/froslew.c
	src/GameSrc/frpipe.c
	src/GameSrc/frpts.c
	src/GameSrc/frsetup.c
	src/GameSrc/frtables.c
	src/GameSrc/frterr.c
	src/GameSrc/frutil.c
	src/GameSrc/FrUtils.c
	src/GameSrc/fullamap.c
	src/GameSrc/fullscrn.c
	src/GameSrc/gameloop.c
	src/GameSrc/gameobj.c
	src/GameSrc/gamesort.c
	src/GameSrc/gamestrn.c
	src/GameSrc/gamesys.c
	src/GameSrc/gametime.c
	src/GameSrc/gamewrap.c
	src/GameSrc/gearmfd.c
	src/GameSrc/gr2ss.c
	src/GameSrc/grenades.c
	src/GameSrc/hand.c
	src/GameSrc/hflip.c
	src/GameSrc/hkeyfunc.c
	src/GameSrc/hud.c
	src/GameSrc/hudobj.c
	src/GameSrc/init.c
	src/GameSrc/input.c
	src/GameSrc/invent.c
	src/GameSrc/leanmetr.c
	src/GameSrc/mainloop.c
	src/GameSrc/map.c
	src/GameSrc/mfdfunc.c
	src/GameSrc/mfdgadg.c
	src/GameSrc/mfdgames.c
	src/GameSrc/mfdgump.c
	src/GameSrc/mfdpanel.c
	src/GameSrc/minimax.c
	src/GameSrc/mlimbs.c
	src/GameSrc/movekeys.c
	src/GameSrc/musicai.c
	src/GameSrc/newai.c
	src/GameSrc/newmfd.c
	src/GameSrc/objapp.c
	src/GameSrc/objects.c
	src/GameSrc/objload.c
	src/GameSrc/objprop.c
	src/GameSrc/objsim.c
	src/GameSrc/objuse.c
	src/GameSrc/olh.c
	src/GameSrc/olhscan.c
	src/GameSrc/palfx.c
	src/GameSrc/pathfind.c
	src/GameSrc/physics.c
	src/GameSrc/player.c
	src/GameSrc/plotware.c
	src/GameSrc/popups.c
	src/GameSrc/render.c
	src/GameSrc/rendtool.c
	src/GameSrc/saveload.c
	src/GameSrc/schedule.c
	src/GameSrc/screen.c
	src/GameSrc/setup.c
	src/GameSrc/shodan.c
	src/GameSrc/sideicon.c
	src/GameSrc/sndcall.c
	src/GameSrc/star.c
	src/GameSrc/statics.c
	src/GameSrc/status.c
	src/GameSrc/target.c
	src/GameSrc/textmaps.c
	src/GameSrc/tickcount.c
	src/GameSrc/tfdirect.c
	src/GameSrc/tfutil.c
	src/GameSrc/tools.c
	src/GameSrc/trigger.c
	src/GameSrc/view360.c
	src/GameSrc/viewhelp.c
	src/GameSrc/vitals.c
	src/GameSrc/vmail.c
	src/GameSrc/wares.c
	src/GameSrc/weapons.c
	src/GameSrc/wrapper.c
	src/GameSrc/gamerend.c
	src/GameSrc/mouselook.c
)

include_directories(
	BEFORE
	src/Libraries/2D/Source
	src/Libraries/3D/Source
	src/Libraries/AFILE/Source
	src/Libraries/DSTRUCT/Source
	src/Libraries/EDMS/Source
	src/Libraries/FIXPP/Source
	src/Libraries/INPUT/Source
	src/Libraries/PALETTE/Source
	src/Libraries/RES/Source
	src/Libraries/UI/Source
	src/Libraries/RND/Source
	src/Libraries/VOX/Source
	src/Libraries/FIX/Source
	src/Libraries/SND/Source
	src/Libraries/H
	src/Libraries/LG/Source
	src/Libraries/LG/Source/LOG/src
	src/Libraries/adlmidi/include
	src/GameSrc/Headers
	src/MacSrc
	src/MusicSrc
	${CMAKE_BINARY_DIR}/src/GameSrc/Headers
)

# Include magic header file, set struct packing size
add_definitions(
	-include precompiled.h
)

add_executable(systemshock
	${MAC_SRC}
)

add_library(GAME_LIB ${GAME_SRC})
target_link_libraries(GAME_LIB PUBLIC
	# SDL 2 Mixer
	$<IF:$<TARGET_EXISTS:SDL2_mixer::SDL2_mixer>,SDL2_mixer::SDL2_mixer,SDL2_mixer::SDL2_mixer-static>
)

# MINGW additional linker options
if(MINGW)
	set(WINDOWS_LIBRARIES "mingw32 -mwindows")
endif(MINGW)

target_link_libraries(systemshock
	${WINDOWS_LIBRARIES} # Set it before any linker options! Beware WinMain@16 error!!
	# SDL 2
	$<TARGET_NAME_IF_EXISTS:SDL2::SDL2main>
	$<IF:$<TARGET_EXISTS:SDL2::SDL2>,SDL2::SDL2,SDL2::SDL2-static>
	# FluidSynth
	$<$<BOOL:${FluidSynth_FOUND}>:FluidSynth::libfluidsynth>
	# OpenGL
	OpenGL::GL
	# ALSA
	$<$<NOT:$<BOOL:${WIN32}>>:ALSA::ALSA>
	GAME_LIB
	UI_LIB
	2D_LIB
	LG_LIB
	GR_LIB
	3D_LIB
	RND_LIB
	AFILE_LIB
	DSTRUCT_LIB
	FIX_LIB
	INPUT_LIB
	PALETTE_LIB
	RES_LIB
#	SND_LIB
	VOX_LIB
	EDMS_LIB
	FIXPP_LIB
	ADLMIDI_LIB
)

# Turn on address sanitizing if wanted
set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/externals/sanitizers/cmake" ${CMAKE_MODULE_PATH})
find_package(Sanitizers)
add_sanitizers(systemshock)
