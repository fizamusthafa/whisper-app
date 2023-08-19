#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "ffi_static" for configuration "Release"
set_property(TARGET ffi_static APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ffi_static PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "ASM_MASM;C"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/ffi.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS ffi_static )
list(APPEND _IMPORT_CHECK_FILES_FOR_ffi_static "${_IMPORT_PREFIX}/lib/ffi.lib" )

# Import target "ffi_shared" for configuration "Release"
set_property(TARGET ffi_shared APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(ffi_shared PROPERTIES
  IMPORTED_IMPLIB_RELEASE "${_IMPORT_PREFIX}/lib/ffi.lib"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/ffi.dll"
  )

list(APPEND _IMPORT_CHECK_TARGETS ffi_shared )
list(APPEND _IMPORT_CHECK_FILES_FOR_ffi_shared "${_IMPORT_PREFIX}/lib/ffi.lib" "${_IMPORT_PREFIX}/bin/ffi.dll" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
