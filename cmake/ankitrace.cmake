if(USE_LRYATRACE AND MATEOS)
    add_compile_options(-DUSE_LRYATRACE)
    find_package(LTTngUST)
    set(LRYATRACE lryatrace)
endif()
