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
		if plug[childName + "Visibility"]["enabled"].getValue() :
			info.append( IECore.CamelCase.toSpaced( childName ) + ( " On" if plug[childName + "Visibility"]["value"].getValue() else " Off" ) )

	return ", ".join( info )

def __shadingSummary( plug ) :

	info = []
	for childName in ( "useHoldout", "isShadowCatcher", "color", "lightGroup" ) :
		if plug[childName]["enabled"].getValue() :
			info.append( IECore.CamelCase.toSpaced( childName ) + ( " On" if plug[childName]["value"].getValue() else " Off" ) )

	return ", ".join( info )

def __subdivisionSummary( plug ) :

	info = []
	for childName in ( "maxLevel", "dicingScale" ) :
		if plug[childName]["enabled"].getValue() :
			info.append( IECore.CamelCase.toSpaced( childName ) + ( " On" if plug[childName]["value"].getValue() else " Off" ) )

	return ", ".join( info )

def __volumeSummary( plug ) :

	info = []
	if plug["volumeIsovalue"]["enabled"].getValue() :
		info.append( IECore.CamelCase.toSpaced( "volumeIsovalue" ) + ( " On" if plug["volumeIsovalue"]["value"].getValue() else " Off" ) )

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
			"layout:section:Subdivision:summary", __subdivisionSummary,
			"layout:section:Volume:summary", __volumeSummary,

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

		"attributes.useHoldout" : [

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

		"attributes.color" : [

			"description",
			"""
			Set a unique color per-object. This is intended for setting
			a unique constant color that can be accessed from an object_info
			shader, even if the object is being instanced.
			""",

			"layout:section", "Shading",
		],

		"attributes.lightGroup" : [

			"description",
			"""
			Set the lightgroup of an object with emission.
			""",

			"layout:section", "Shading",
		],

		# Subdivision

		"attributes.maxLevel" : [

			"description",
			"""
			The max level of subdivision that can be
			applied.
			""",

			"layout:section", "Subdivision",

		],

		"attributes.dicingScale" : [

			"description",
			"""
			Multiplier for scene dicing rate.
			""",

			"layout:section", "Subdivision",

		],

		# Volume

		"attributes.volumeIsovalue" : [

			"description",
			"""
			Set the volume isovalue.
			""",

			"layout:section", "Volume",

		],

	}

)

if not GafferCycles.withLightGroups :

	Gaffer.Metadata.registerValue( GafferCycles.CyclesOptions, "attributes.lightGroup", "plugValueWidget:type", "" )

if not GafferCycles.withOpenVDB :

	Gaffer.Metadata.registerValue( GafferCycles.CyclesOptions, "attributes.volumeIsovalue", "plugValueWidget:type", "" )
