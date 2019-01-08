##########################################################################
#
#  Copyright (c) 2018, Alex Fuller. All rights reserved.
#  Copyright (c) 2013, Image Engine Design Inc. All rights reserved.
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

import functools
import collections

import IECore

import Gaffer
import GafferUI
import GafferCycles

##########################################################################
# Build a registry of information retrieved from GafferCycles metadata.
##########################################################################

def __outPlugNoduleType( plug ) :

	return "GafferUI::CompoundNodule" if len( plug ) else "GafferUI::StandardNodule"

def __getSocketToWidget( socketType ) :
	if( socketType == "boolean" ) :
		return "GafferUI.BoolPlugValueWidget"
	elif( socketType == "float" ) :
		return "GafferUI.NumericPlugValueWidget"
	elif( socketType == "int" ) :
		return "GafferUI.NumericPlugValueWidget"
	elif( socketType == "uint" ) :
		return "GafferUI.NumericPlugValueWidget"
	elif( socketType == "color" ) :
		return "GafferUI.ColorPlugValueWidget"
	#elif( socketType == "vector" ) :
	#	return "GafferUI.NumericPlugValueWidget"
	#elif( socketType == "point" ) :
	#	return "GafferUI.NumericPlugValueWidget"
	#elif( socketType == "normal" ) :
	#	return "GafferUI.NumericPlugValueWidget"
	#elif( socketType == "point2" ) :
	#	return "GafferUI.NumericPlugValueWidget"
	#elif( socketType == "closure" ) :
	#	return "GafferUI.StringPlugValueWidget"
	elif( socketType == "string" ) :
		return "GafferUI.StringPlugValueWidget"
	elif( socketType == "enum" ) :
		return "GafferUI.PresetsPlugValueWidget"
	#elif( socketType == "transform" ) :
	#	return "GafferUI.NumericPlugValueWidget"
	#elif( socketType == "node" ) :
	#	return "GafferUI.StringPlugValueWidget"
	else :
		return ""

__metadata = collections.defaultdict( dict )

def __translateParamMetadata( nodeTypeName, socketName, value ) :
	paramPath = nodeTypeName + ".parameters." + socketName
	socketType = value["type"]
	label = value["ui_name"]
	flags = value["flags"]
	if socketType == "enum" :
		presetNames = IECore.StringVectorData()
		presetValues = IECore.IntVectorData()
		for enumName, enumValues in value["enum_values"].items() :
			presetNames.append(enumName)
			presetValues.append(enumValues)
		__metadata[paramPath]["presetNames"] = presetNames
		__metadata[paramPath]["presetValues"] = presetValues

	__metadata[paramPath]["plugValueWidget:type"] = __getSocketToWidget( socketType )

	if( socketName == "filename" ) :
		__metadata[paramPath]["plugValueWidget:type"] = "GafferUI.PathPlugValueWidget"

	__metadata[paramPath]["noduleLayout:visible"] = True
	__metadata[paramPath]["label"] = label
	# Linkable
	linkable = bool( flags & ( 1 << 0 ) )
	__metadata[paramPath]["nodule:type"] = "GafferUI::StandardNodule" if linkable else ""

	if "category" in value :
		__metadata[paramPath]["layout:section"] = value["category"]

def __translateShaderMetadata() :

	for socketName, value in GafferCycles.nodes["shader"]["in"].items() :
		__translateParamMetadata( "output", socketName, value )

def __translateNodesMetadata( nodeTypes ) :

	for nodeTypeName, nodeType in nodeTypes.items() :
		# Inputs
		for socketName, value in nodeType["in"].items() :
			__translateParamMetadata( nodeTypeName, socketName, value )

__translateShaderMetadata() # For the main interfacing 'shader' node
__translateNodesMetadata( GafferCycles.lights )
__translateNodesMetadata( GafferCycles.shaders )

##########################################################################
# Gaffer Metadata queries. These are implemented using the preconstructed
# registry above.
##########################################################################

def __nodeDescription( node ) :

	if isinstance( node, GafferCycles.CyclesShader ) :
		return __metadata[node["name"].getValue()].get(
			"description",
			"""Loads shaders for use in Cycles renders. Use the ShaderAssignment node to assign shaders to objects in the scene.""",
		)
	else :
		return __metadata[node["__shaderName"].getValue()].get(
			"description",
			"""Loads an Cycles light shader and uses it to output a scene with a single light."""
		)

def __nodeMetadata( node, name ) :

	if isinstance( node, GafferCycles.CyclesShader ) :
		key = node["name"].getValue()
	else :
		# Node type is CyclesLight.
		key = node["__shaderName"].getValue()

	return __metadata[key].get( name )

def __plugMetadata( plug, name ) :

	if name == "noduleLayout:visible" and plug.getInput() is not None :
		# Before the introduction of nodule visibility controls,
		# users may have made connections to plugs which are now
		# hidden by default. Make sure we continue to show them
		# by default - they can still be hidden explicitly by
		# adding an instance metadata value.
		return True

	node = plug.node()
	if isinstance( node, GafferCycles.CyclesShader ) :
		key = plug.node()["name"].getValue() + "." + plug.relativeName( node )
	else :
		# Node type is ArnoldLight.
		key = plug.node()["__shaderName"].getValue() + "." + plug.relativeName( node )

	return __metadata[key].get( name )

for nodeType in ( GafferCycles.CyclesShader, GafferCycles.CyclesLight ) :

	nodeKeys = set()
	parametersPlugKeys = set()
	parameterPlugKeys = set()

	for name, metadata in __metadata.items() :
		keys = ( nodeKeys, parametersPlugKeys, parameterPlugKeys )[name.count( ".")]
		keys.update( metadata.keys() )

	for key in nodeKeys :
		Gaffer.Metadata.registerValue( nodeType, key, functools.partial( __nodeMetadata, name = key ) )

	for key in parametersPlugKeys :
		Gaffer.Metadata.registerValue( nodeType, "parameters", key, functools.partial( __plugMetadata, name = key ) )

	for key in parameterPlugKeys :
		Gaffer.Metadata.registerValue( nodeType, "parameters.*", key, functools.partial( __plugMetadata, name = key ) )

	Gaffer.Metadata.registerValue( nodeType, "description", __nodeDescription )

Gaffer.Metadata.registerValue( GafferCycles.CyclesShader, "attributeSuffix", "plugValueWidget:type", "GafferUI.StringPlugValueWidget" )
Gaffer.Metadata.registerValue( GafferCycles.CyclesShader, "attributeSuffix", "layout:visibilityActivator", "suffixActivator" )

Gaffer.Metadata.registerNode( 

	GafferCycles.CyclesShader, 

	plugs = {

		"out" : [

			"nodule:type", __outPlugNoduleType,
			"noduleLayout:spacing", 0.2,

		],

		"out.*" : [

			"noduleLayout:visible", True,

		]
	}
)
