function(import target rel_subdir)
  if(NOT TARGET ${target})
    message(STATUS "target: " ${target} " " ${rel_subdir})
    add_subdirectory("${rel_subdir}")
  endif()
endfunction()