'''OpenGL extension NV.blend_square

This module customises the behaviour of the 
OpenGL.raw.GL.NV.blend_square to provide a more 
Python-friendly API

Overview (from the spec)
	
	It is useful to be able to multiply a number by itself in the blending
	stages -- for example, in certain types of specular lighting effects
	where a result from a dot product needs to be taken to a high power.
	
	This extension provides four additional blending factors to permit
	this and other effects: SRC_COLOR and ONE_MINUS_SRC_COLOR for source
	blending factors, and DST_COLOR and ONE_MINUS_DST_COLOR for destination
	blending factors.
	
	Direct3D provides capability bits for advertising these additional
	blend modes.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/blend_square.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.blend_square import *
from OpenGL.raw.GL.NV.blend_square import _EXTENSION_NAME

def glInitBlendSquareNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION