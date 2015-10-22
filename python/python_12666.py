# boost python wrapper in dynamic library undefined reference
#   define BOOST_PYTHON_MODULE_INIT(name)                               \
  void BOOST_PP_CAT(init_module_,name)();                               \
extern "C" __attribute__ ((__visibility__("default"))) _BOOST_PYTHON_MODULE_INIT(name)
