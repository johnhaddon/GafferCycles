##########################################################################
#
#  Copyright (c) 2018, Alex Fuller. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import IECore

import Gaffer
import GafferCycles

def __visibilitySummary( plug ) :

	info = []
	for childName in ( "camera", "diffuse", "glossy", "transmission", "shadow", "scatter" ) :
		if plug[childName]["enabled"].getValue() :
			info.append( IECore.CamelCase.toSpaced( childName ) + ( " On" if plug[childName]["value"].getValue() else " Off" ) )

	return ", ".join( info )

def __shadingSummary( plug ) :

	info = []
	for childName in ( "matte", "isShadowCatcher" ) :
		if plug[childName]["enabled"].getValue() :
			info.append( IECore.CamelCase.toSpaced( childName ) + ( " On" if plug[childName]["value"].getValue() else " Off" ) )

	return ", ".join( info )

Gaffer.Metadata.registerNode(

	GafferCycles.CyclesAttributes,

	"description",
	"""
	Applies Cycles attributes to objects in the scene.
	""",

	plugs = {

		# Sections

		"attributes" : [

			"layout:section:Visibility:summary", __visibilitySummary,
			"layout:section:Shading:summary", __shadingSummary,

		],

		# Visibility

		"attributes.cameraVisibility" : [

			"description",
			"""
			Whether or not the object is visible to camera
			rays. To hide an object completely, use the
			visibility settings on the StandardAttributes
			node instead.
			""",

			"layout:section", "Visibility",
			"label", "Camera",

		],

		"attributes.diffuseVisibility" : [

			"description",
			"""
			Whether or not the object is visible to diffuse
			rays.
			""",

			"layout:section", "Visibility",
			"label", "Diffuse",

		],

		"attributes.glossyVisibility" : [

			"description",
			"""
			Whether or not the object is visible in
			glossy rays.
			""",

			"layout:section", "Visibility",
			"label", "Glossy",

		],

		"attributes.transmissionVisibility" : [

			"description",
			"""
			Whether or not the object is visible in
			transmission.
			""",

			"layout:section", "Visibility",
			"label", "Transmission",

		],

		"attributes.shadowVisibility" : [

			"description",
			"""
			Whether or not the object is visible to shadow
			rays - whether it casts shadows or not.
			""",

			"layout:section", "Visibility",
			"label", "Shadow",

		],

		"attributes.scatterVisibility" : [

			"description",
			"""
			Whether or not the object is visible to
			scatter rays.
			""",

			"layout:section", "Visibility",
			"label", "Scatter",

		],

		# Shading

		"attributes.matte" : [

			"description",
			"""
			Turns the object into a holdout matte.
			This only affects primary (camera) rays.
			""",

			"layout:section", "Shading",

		],

		"attributes.isShadowCatcher" : [

			"description",
			"""
			Turns the object into a shadow catcher.
			""",

			"layout:section", "Shading",

		],

	}

)
