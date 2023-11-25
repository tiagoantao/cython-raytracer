from Cython.Build import cythonize

compiler_directives = {"language_level": 3, "embedsignature": True}


def build(setup_kwargs):
    setup_kwargs.update(
        {
            "name": "cython-raytracer",
            "package": ["cython_raytracer"],
            "ext_modules": cythonize(
                module_list="cython_raytracer/rt/**/*.py",
                compiler_directives=compiler_directives,
            ),
        }
    )

