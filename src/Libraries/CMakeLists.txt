enable_language(ASM)
set(can_use_assembler TRUE)

set(2D_SRC
	2D/Source/bit.c
	2D/Source/bitmap.c
	2D/Source/blend.c
	2D/Source/canvas.c
	2D/Source/close.c
	2D/Source/cnvtab.c
	2D/Source/context.c
	2D/Source/detect.c
	2D/Source/devtab.c
	2D/Source/fcntab.c
	2D/Source/init.c
	2D/Source/lintab.c
	2D/Source/mode.c
	2D/Source/pal.c
	2D/Source/permap.c
	2D/Source/persetup.c
	2D/Source/pertol.c
	2D/Source/rgb.c
	2D/Source/screen.c
	2D/Source/sscrn.c
	2D/Source/StateStk.c
	2D/Source/svgainit.c
	2D/Source/tempbm.c
	2D/Source/temptm.c
	2D/Source/tlucdat.c
	2D/Source/tluctab.c
	2D/Source/valloc.c
	2D/Source/vtab.c
	2D/Source/MacDev.c
	2D/Source/GR/grilin.c
	2D/Source/GR/grmalloc.c
	2D/Source/GR/grnull.c
	2D/Source/GR/gruilin.c
	2D/Source/GR/grd.c
	2D/Source/Gen/gendisk.c
	2D/Source/Gen/gentm.c
	2D/Source/Gen/genwclin.c
	2D/Source/Gen/genuclin.c
	2D/Source/Gen/genrsd8.c
	2D/Source/Gen/genuvlin.c
	2D/Source/Gen/genhlin.c
	2D/Source/Gen/genrsdbm.c
	2D/Source/Gen/genvlin.c
	2D/Source/Gen/genvcply.c
	2D/Source/Gen/genclin.c
	2D/Source/Gen/genfl8c.c
	2D/Source/Gen/genrsdtm.c
	2D/Source/Gen/genel.c
	2D/Source/Gen/genwlin.c
	2D/Source/Gen/genpix.c
	2D/Source/Gen/genuhlin.c
	2D/Source/Gen/genhfl8.c
	2D/Source/Gen/genov.c
	2D/Source/Gen/gente.c
	2D/Source/Gen/genlin.c
	2D/Source/Gen/gencwlin.c
	2D/Source/Gen/genchfl8.c
	2D/Source/Gen/gengfl8.c
	2D/Source/Gen/genbox.c
	2D/Source/Gen/genmono.c
	2D/Source/Gen/genulin.c
	2D/Source/Gen/gencnv.c
	2D/Source/Gen/genuslin.c
	2D/Source/Gen/genvpoly.c
	2D/Source/Gen/general.c
	2D/Source/Gen/gencirc.c
	2D/Source/Gen/genfl8.c
	2D/Source/Gen/genf24.c
	2D/Source/Gen/gentl8.c
	2D/Source/Gen/genrect.c
	2D/Source/Gen/genvrect.c
	2D/Source/Gen/genslin.c
	2D/Source/Flat8/fl8vlin.c
	2D/Source/Flat8/FL8OPL.c
	2D/Source/Flat8/fl8cply.c
	2D/Source/Flat8/fl8clin.c
	2D/Source/Flat8/fl8lp.c
	2D/Source/Flat8/fl8lf.c
	2D/Source/Flat8/fl8ll.c
	2D/Source/Flat8/fl8s.c
	2D/Source/Flat8/fl8hfl8.c
	2D/Source/Flat8/fl8pnt.c
	2D/Source/Flat8/fl8fl8m.c
	2D/Source/Flat8/fl8ltp.c
	2D/Source/Flat8/fl8fl8c.c
	2D/Source/Flat8/fl8w.c
	2D/Source/Flat8/fl8cop.c
	2D/Source/Flat8/fl8wlin.c
	2D/Source/Flat8/fl8lw.c
	2D/Source/Flat8/fl8pix.c
	2D/Source/Flat8/fl8row.c
	2D/Source/Flat8/fl8ft.c
	2D/Source/Flat8/fl8rsd8.c
	2D/Source/Flat8/Fl8F.c
	2D/Source/Flat8/fl8bldbl.c
	2D/Source/Flat8/fl8clear.c
	2D/Source/Flat8/fl8p.c
	2D/Source/Flat8/fl8wclin.c
	2D/Source/Flat8/fl8hlin.c
	2D/Source/Flat8/fl8bl.c
	2D/Source/Flat8/fl8gpix.c
	2D/Source/Flat8/fl8ns.c
	2D/Source/Flat8/fl8lnop.c
	2D/Source/Flat8/fl8dbl.c
	2D/Source/Flat8/fl8clin.h
	2D/Source/Flat8/fl8cnv.c
	2D/Source/Flat8/fl8slin.c
	2D/Source/Flat8/fl8lin.c
	2D/Source/Flat8/fl8tsmap.c
	2D/Source/Flat8/fl8ply.c
	2D/Source/Flat8/fl8sply.c
	2D/Source/Flat8/fl8rect.c
	2D/Source/Flat8/fl8gfl8.c
	2D/Source/Flat8/fl8tl8.c
	2D/Source/Flat8/fl8p24.c
	2D/Source/Flat8/fl8g24.c
	2D/Source/Flat8/fl8ctp.c
	2D/Source/Flat8/fl8mscl.c
	2D/Source/Flat8/fl8lop.c
	2D/Source/Flat8/fl8ntrp2.c
	2D/Source/Flat8/fl8sub.c
	2D/Source/Flat8/fl8tpl.c
	2D/Source/Flat8/fl8wclin.h
	2D/Source/Flat8/fl8nl.c
	2D/Source/Flat8/fl8fltr2.c
	2D/Source/Flat8/fl8mono.c
	2D/Source/Flat8/fl8fl8.c
	2D/Source/Flat8/fl8chfl8.c
	2D/Source/Clip/clpply.c
	2D/Source/Clip/clplin.c
	2D/Source/Clip/clpclin.c
	2D/Source/Clip/clpltab.c
	2D/Source/Clip/clpf24.c
	2D/Source/Clip/clplin2.c
	2D/Source/Clip/clppoly.c
	2D/Source/Clip/clpslin.c
	2D/Source/Clip/clprect.c
	2D/Source/Clip/clpmono.c
	2D/Source/RSD/rsdcvt.c
	2D/Source/RSD/RSDUnpack.c
	2D/Source/string/chrsiz.c
	2D/Source/string/genchr.c
	2D/Source/string/genstr.c
	2D/Source/string/genuchr.c
	2D/Source/string/genustr.c
	2D/Source/string/strscl.c
	2D/Source/string/strsiz.c
	2D/Source/string/struscl.c
	2D/Source/string/strwrap.c
)

set(GR_SRC
	2D/Source/GR/grd.c
	2D/Source/GR/grilin.c
	2D/Source/GR/grmalloc.c
	2D/Source/GR/grnull.c
	2D/Source/GR/gruilin.c
)


set(3D_SRC
	3D/Source/alloc.c
	3D/Source/Bitmap.c
	3D/Source/clip.c
	3D/Source/detail.c
	3D/Source/fov.c
	3D/Source/GlobalV.c
	3D/Source/instance.c
	3D/Source/interp.c
	3D/Source/light.c
	3D/Source/matrix.c
	3D/Source/points.c
	3D/Source/polygon.c
	3D/Source/slew.c
	3D/Source/tmap.c
	3D/Source/vector.c
)

set(AFILE_SRC
	AFILE/Source/afile.c
	AFILE/Source/amov.c
	AFILE/Source/compose.c
	AFILE/Source/draw4x4.cpp
	AFILE/Source/huffde.cpp
	AFILE/Source/movie.c)

set(DSTRUCT_SRC
	DSTRUCT/Source/array.c
	DSTRUCT/Source/hash.c
	DSTRUCT/Source/pqueue.c
	DSTRUCT/Source/rect.c
)


set(FIX_SRC
	FIX/Source/f_exp.c
	FIX/Source/fix.c
	FIX/Source/fix_pow.c
	FIX/Source/fix_sqrt.c
	FIX/Source/MakeTables.c
)

set(INPUT_SRC
	INPUT/Source/kbcook.c
	INPUT/Source/mouse.c
	INPUT/Source/sdl_events.c
)

set(LG_SRC
	LG/Source/LOG/src/log.c
	LG/Source/memall.c
	LG/Source/stack.c
	LG/Source/tmpalloc.c
)

set(PALETTE_SRC
        PALETTE/Source/palette.c
)

set(RES_SRC
	RES/Source/caseless.c
	RES/Source/lzw.c
	RES/Source/refacc.c
	RES/Source/resacc.c
	RES/Source/resbuild.c
	RES/Source/res.c
	RES/Source/resfile.c
	RES/Source/resformat.c
	RES/Source/resload.c
	RES/Source/resmake.c
	RES/Source/restypes.c
)

set(RND_SRC
	RND/Source/rnd.c
)

set(SND_SRC
	SND/Source/dig_init.c
	SND/Source/dig_ops.c
	SND/Source/master.c
	SND/Source/mid_init.c
	SND/Source/mid_ops.c
	SND/Source/snd_util.c
)

set(UI_SRC
	UI/Source/curdrw.c
	UI/Source/cursors.c
	UI/Source/event.c
	UI/Source/hotkey.c
	UI/Source/region.c
	UI/Source/slab.c
	UI/Source/vmouse.c
)

set(FIXPP_SRC
	FIXPP/Source/fixpp.cpp
)

set(EDMS_SRC
	EDMS/Source/interfac.cc
	EDMS/Source/collide.cc
	EDMS/Source/intrsect.cc
	EDMS/Source/globals.cc
	EDMS/Source/phy_tool.cc
	EDMS/Source/soliton.cc
	EDMS/Source/MODELS/robot.cc
	EDMS/Source/MODELS/pelface.cc
	EDMS/Source/MODELS/ftl.cc
	EDMS/Source/MODELS/pelvis.cc
	EDMS/Source/MODELS/d_frame.cc
	EDMS/Source/MODELS/d_f_face.cc
	EDMS/Source/MODELS/ftlface.cc
	EDMS/Source/MODELS/d_f_2.cc
)

set(ADLMIDI_SRC
	adlmidi/adlmidi_sequencer.cpp
	adlmidi/adlmidi_bankmap.tcc
	adlmidi/cvt_mus2mid.hpp
	adlmidi/adlmidi_bankmap.h
	adlmidi/midi_sequencer.hpp
	adlmidi/chips/dosbox_opl3.h
	adlmidi/chips/opl_chip_base.h
	adlmidi/chips/nuked_opl3.h
	adlmidi/chips/dosbox/dbopl.h
	adlmidi/chips/dosbox/dbopl.cpp
	adlmidi/chips/dosbox_opl3.cpp
	adlmidi/chips/nuked_opl3_v174.cpp
	adlmidi/chips/nuked/nukedopl3_174.c
	adlmidi/chips/nuked/nukedopl3.c
	adlmidi/chips/nuked/nukedopl3_174.h
	adlmidi/chips/nuked/nukedopl3.h
	adlmidi/chips/opl_chip_base.tcc
	adlmidi/chips/nuked_opl3.cpp
	adlmidi/chips/nuked_opl3_v174.h
	adlmidi/wopl/wopl_file.c
	adlmidi/wopl/wopl_file.h
	adlmidi/include/adlmidi.hpp
	adlmidi/include/adlmidi.h
	adlmidi/adlmidi_private.hpp
	adlmidi/file_reader.hpp
	adlmidi/adlmidi_ptr.hpp
	adlmidi/adlmidi_opl3.cpp
	adlmidi/midi_sequencer_impl.hpp
	adlmidi/adldata.hh
	adlmidi/adlmidi_private.cpp
	adlmidi/adlmidi_midiplay.cpp
	adlmidi/adlmidi.cpp
	adlmidi/cvt_xmi2mid.hpp
	adlmidi/adlmidi_load.cpp
	adlmidi/adldata.cpp
	adlmidi/fraction.hpp
	adlmidi/midi_sequencer.h
)

set(VOX_SRC
	VOX/Source/vox2d.c
	VOX/Source/vox3d.c
	VOX/Source/voxinit.c
)

include_directories(
	${CMAKE_SOURCE_DIR}/src/GameSrc/Headers
	${CMAKE_SOURCE_DIR}/src/MacSrc
	${CMAKE_SOURCE_DIR}/src/Libraries/adlmidi/include
	${CMAKE_SOURCE_DIR}/src/Libraries/2D/Source/GR
	${CMAKE_SOURCE_DIR}/src/Libraries/2D/Source/Clip
	${CMAKE_SOURCE_DIR}/src/Libraries/2D/Source/Flat8
	${CMAKE_SOURCE_DIR}/src/Libraries/2D/Source/Gen
	${CMAKE_SOURCE_DIR}/src/Libraries/2D/Source/RSD
	${CMAKE_SOURCE_DIR}/src/Libraries/2D/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/3D/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/AFILE/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/DSTRUCT/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/H
	${CMAKE_SOURCE_DIR}/src/Libraries/INPUT/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/FIX/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/LG/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/LG/Source/LOG/src
	${CMAKE_SOURCE_DIR}/src/Libraries/RES/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/FIXPP/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/EDMS/Source
	${CMAKE_SOURCE_DIR}/src/Libraries/EDMS/Source/MODELS
)

add_library(2D_LIB ${2D_SRC})
target_link_libraries(2D_LIB LG_LIB)
add_library(GR_LIB ${GR_SRC})
add_library(3D_LIB ${3D_SRC})
target_link_libraries(3D_LIB OpenGL::GL m)
add_library(AFILE_LIB ${AFILE_SRC})
target_link_libraries(AFILE_LIB 2D_LIB RES_LIB)
add_library(PALETTE_LIB ${PALETTE_SRC})
add_library(DSTRUCT_LIB ${DSTRUCT_SRC})
add_library(FIX_LIB ${FIX_SRC})
target_link_libraries(FIX_LIB LG_LIB m)
add_library(INPUT_LIB ${INPUT_SRC})
target_link_libraries(INPUT_LIB PUBLIC
	# SDL 2
	$<TARGET_NAME_IF_EXISTS:SDL2::SDL2main>
	$<IF:$<TARGET_EXISTS:SDL2::SDL2>,SDL2::SDL2,SDL2::SDL2-static>
)
add_library(LG_LIB ${LG_SRC})
add_library(RES_LIB ${RES_SRC})
add_library(RND_LIB ${RND_SRC})
add_library(UI_LIB ${UI_SRC})
target_link_libraries(UI_LIB PUBLIC
	# SDL 2
	$<TARGET_NAME_IF_EXISTS:SDL2::SDL2main>
	$<IF:$<TARGET_EXISTS:SDL2::SDL2>,SDL2::SDL2,SDL2::SDL2-static>
)
add_library(VOX_LIB ${VOX_SRC})
add_library(FIXPP_LIB ${FIXPP_SRC})
add_library(EDMS_LIB ${EDMS_SRC})
add_library(ADLMIDI_LIB ${ADLMIDI_SRC})
