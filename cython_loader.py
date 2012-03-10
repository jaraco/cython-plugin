
import Cython.Distutils.build_ext

def set_build_ext(dist, attr, value):
	if not value:
		return
	dist.cmdclass.setdefault(Cython.Distutils.build_ext)
