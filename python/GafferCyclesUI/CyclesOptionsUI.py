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
import GafferUI
import GafferCycles

def __sessionSummary( plug ) :

	info = []

	if plug["device"]["enabled"].getValue() :
		info.append( "Device {}".format( plug["device"]["value"].getValue() ) )

	if plug["featureSet"]["enabled"].getValue() :
		if plug["featureSet"]["value"].getValue() :
			info.append( "Experimental Features" )
		else :
			info.append( "Standard Features" )

	if plug["shadingSystem"]["enabled"].getValue() :
		info.append( "Shading System {}".format( plug["shadingSystem"]["value"].getValue() ) )

	if plug["numThreads"]["enabled"].getValue() :
		info.append( "Threads {}".format( plug["numThreads"]["value"].getValue() ) )

	if plug["tileOrder"]["enabled"].getValue() :
		info.append(
			"Tile Order {}".format( Gaffer.NodeAlgo.currentPreset( plug["tileOrder"]["value"] ) )
		)

	if plug["tileSize"]["enabled"].getValue() :
		info.append(
			"Tile Size {}".format( Gaffer.NodeAlgo.currentPreset( plug["tileSize"]["value"] ) )
		)

	if plug["startResolution"]["enabled"].getValue() :
		info.append(
			"Start Resolution {}".format( Gaffer.NodeAlgo.currentPreset( plug["startResolution"]["value"] ) )
		)

	if plug["pixelSize"]["enabled"].getValue() :
		info.append(
			"Pixel Size {}".format( Gaffer.NodeAlgo.currentPreset( plug["pixelSize"]["value"] ) )
		)

	if plug["cancelTimeout"]["enabled"].getValue() :
		info.append(
			"Cancel Timeout {}".format( Gaffer.NodeAlgo.currentPreset( plug["cancelTimeout"]["value"] ) )
		)

	if plug["resetTimeout"]["enabled"].getValue() :
		info.append(
			"Reset Timeout {}".format( Gaffer.NodeAlgo.currentPreset( plug["resetTimeout"]["value"] ) )
		)

	if plug["textTimeout"]["enabled"].getValue() :
		info.append(
			"Text Timeout {}".format( Gaffer.NodeAlgo.currentPreset( plug["textTimeout"]["value"] ) )
		)

	if plug["progressiveUpdateTimeout"]["enabled"].getValue() :
		info.append(
			"Progressive Update Timeout {}".format( Gaffer.NodeAlgo.currentPreset( plug["progressiveUpdateTimeout"]["value"] ) )
		)

	return ", ".join( info )

def __sceneSummary( plug ) :

	info = []

	if plug["bvhLayout"]["enabled"].getValue() :
		info.append( "BVH Layout {}".format( plug["bvhLayout"]["value"].getValue() ) )

	if plug["useBvhSpatialSplit"]["enabled"].getValue() :
		info.append( "Use BVH Spatial Splits {}".format( plug["useBvhSpatialSplit"]["value"].getValue() ) )

	if plug["useBvhUnalignedNodes"]["enabled"].getValue() :
		info.append( "Use BVH Unaligned Nodes {}".format( plug["useBvhUnalignedNodes"]["value"].getValue() ) )

	if plug["numBvhTimeSteps"]["enabled"].getValue() :
		info.append( "Num BVH Time Steps {}".format( plug["numBvhTimeSteps"]["value"].getValue() ) )

	if plug["textureLimit"]["enabled"].getValue() :
			info.append( "Texture Limit - {}".format( plug["textureLimit"]["value"].getValue() ) )

	return ", ".join( info )

def __samplingSummary( plug ) :

	info = []

	if plug["method"]["enabled"].getValue() :
		if plug["method"]["value"].getValue() == 0 :
			info.append( "Branched-Path Integrator" )
		elif plug["method"]["value"].getValue() == 1 :
			info.append( "Path Integrator" )

	if plug["samples"]["enabled"].getValue() :
		info.append( "Samples {}".format( plug["samples"]["value"].getValue() ) )

	for sampleType in ( "Diffuse", "Glossy", "Transmission", "AO", "MeshLight", "Subsurface", "Volume" ) :
		childName = "%sSamples" % sampleType.lower()
		if plug[childName]["enabled"].getValue() :
			info.append(
				"{} {}".format( sampleType, plug[childName]["value"].getValue() )
			)

	if plug["samplingPattern"]["enabled"].getValue() :
		info.append( "Sampling Pattern {}".format( plug["samplingPattern"]["value"].getValue() ) )

	if plug["sampleAllLightsDirect"]["enabled"].getValue() :
		info.append( "All Lights Direct {}".format( plug["sampleAllLightsDirect"]["value"].getValue() ) )

	if plug["sampleAllLightsIndirect"]["enabled"].getValue() :
		info.append( "All Lights Indirect {}".format( plug["sampleAllLightsIndirect"]["value"].getValue() ) )

	if plug["lightSamplingThreshold"]["enabled"].getValue() :
		info.append( "Light Sampling Threshold {}".format( plug["lightSamplingThreshold"]["value"].getValue() ) )

	if plug["filterGlossy"]["enabled"].getValue() :
		info.append( "Filter Glossy {}".format( plug["filterGlossy"]["value"].getValue() ) )

	if plug["seed"]["enabled"].getValue() :
		info.append( "Seed Value {}".format( plug["seed"]["value"].getValue() ) )

	if plug["sampleClampDirect"]["enabled"].getValue() :
		info.append( "Sample Clamp Direct {}".format( plug["sampleClampDirect"]["value"].getValue() ) )

	if plug["sampleClampIndirect"]["enabled"].getValue() :
		info.append( "Sample Clamp Indirect {}".format( plug["sampleClampIndirect"]["value"].getValue() ) )

	if plug["startSample"]["enabled"].getValue() :
		info.append( "Start Sample {}".format( plug["startSample"]["value"].getValue() ) )

	return ", ".join( info )

def __rayDepthSummary( plug ) :

	info = []

	if plug["maxBounce"]["enabled"].getValue() :
		info.append( "Max Bounces {}".format( plug["maxBounce"]["value"].getValue() ) )

	for rayType in ( "Diffuse", "Glossy", "Transmission", "Volume" ) :
		childName = "max%sBounce" % rayType
		if plug[childName]["enabled"].getValue() :
			info.append(
				"{} {}".format( rayType, plug[childName]["value"].getValue() )
			)

	if plug["transparentMaxBounce"]["enabled"].getValue() :
		info.append( "Transparency {}".format( plug["transparentMaxBounce"]["value"].getValue() ) )

	return ", ".join( info )

def __volumesSummary( plug ) :

	info = []

	if plug["volumeStepSize"]["enabled"].getValue() :
		info.append( "Step Size {}".format( plug["volumeStepSize"]["value"].getValue() ) )

	if plug["volumeMaxSteps"]["enabled"].getValue() :
		info.append( "Max Steps {}".format( plug["volumeMaxSteps"]["value"].getValue() ) )

	return ", ".join( info )

def __causticsSummary( plug ) :

	info = []

	if plug["causticsReflective"]["enabled"].getValue() :
		info.append( "Reflective Caustics {}".format( plug["causticsReflective"]["value"].getValue() ) )

	if plug["causticsRefractive"]["enabled"].getValue() :
		info.append( "Refractive Caustics {}".format( plug["causticsRefractive"]["value"].getValue() ) )

	return ", ".join( info )

def __subdivisionSummary( plug ) :

	info = []

	if plug["dicingRate"]["enabled"].getValue() :
		info.append( "Dicing Rate {}".format( plug["dicingRate"]["value"].getValue() ) )

	if plug["maxSubdivisions"]["enabled"].getValue() :
		info.append( "Max Subdivisions {}".format( plug["maxSubdivisions"]["value"].getValue() ) )

	if plug["dicingCamera"]["enabled"].getValue() :
		info.append( "Dicing Camera {}".format( plug["dicingCamera"]["value"].getValue() ) )

	if plug["offscreenDicingScale"]["enabled"].getValue() :
		info.append( "Offscreen Dicing Scale {}".format( plug["offscreenDicingScale"]["value"].getValue() ) )

	return ", ".join( info )

def __filmSummary( plug ) :

	info = []

	if plug["exposure"]["enabled"].getValue() :
		info.append( "Exposure {}".format( plug["exposure"]["value"].getValue() ) )

	if plug["passAlphaThreshold"]["enabled"].getValue() :
		info.append( "Pass Alpha Threshold {}".format( plug["passAlphaThreshold"]["value"].getValue() ) )

	if plug["filterType"]["enabled"].getValue() :
		info.append( "Filter Type {}".format( plug["filterType"]["value"].getValue() ) )

	if plug["filterWidth"]["enabled"].getValue() :
		info.append( "Filter Width {}".format( plug["filterWidth"]["value"].getValue() ) )

	if plug["mistStart"]["enabled"].getValue() :
		info.append( "Mist Start {}".format( plug["mistStart"]["value"].getValue() ) )

	if plug["mistDepth"]["enabled"].getValue() :
		info.append( "Mist Depth {}".format( plug["mistDepth"]["value"].getValue() ) )

	if plug["mistFalloff"]["enabled"].getValue() :
		info.append( "Mist Falloff {}".format( plug["mistFalloff"]["value"].getValue() ) )

	if plug["useSampleClamp"]["enabled"].getValue() :
		info.append( "Use Sample Clamp {}".format( plug["useSampleClamp"]["value"].getValue() ) )

	if plug["denoisingDataPass"]["enabled"].getValue() :
		info.append( "Denoising Data Pass {}".format( plug["denoisingDataPass"]["value"].getValue() ) )

	if plug["denoisingCleanPass"]["enabled"].getValue() :
		info.append( "Denoising Clean Pass {}".format( plug["denoisingCleanPass"]["value"].getValue() ) )

	return ", ".join( info )

def __denoisingSummary( plug ) :

	info = []

	if plug["runDenoising"]["enabled"].getValue() :
		info.append( "Run Denoising {}".format( plug["runDenoising"]["value"].getValue() ) )

	for rayType in ( "Diffuse", "Glossy", "Transmission", "Subsurface" ) :
		for dirType in ( "Direct", "Indirect") :
			childName = "denoising%s%s" % ( rayType, dirType )
			if plug[childName]["enabled"].getValue() :
				info.append(
					"{} {} {}".format( rayType, dirType, plug[childName]["value"].getValue() )
				)

	if plug["denoiseStrength"]["enabled"].getValue() :
		info.append( "Strength {}".format( plug["denoiseStrength"]["value"].getValue() ) )

	if plug["denoiseFeatureStrength"]["enabled"].getValue() :
		info.append( "Feature Strength {}".format( plug["denoiseFeatureStrength"]["value"].getValue() ) )

	if plug["denoiseRadius"]["enabled"].getValue() :
		info.append( "Radius {}".format( plug["denoiseRadius"]["value"].getValue() ) )

	if plug["denoiseRelativePca"]["enabled"].getValue() :
		info.append( "Relative Filter {}".format( plug["denoiseRelativePca"]["value"].getValue() ) )

	if plug["denoiseNeighborFrames"]["enabled"].getValue() :
		info.append( "Neighbor Frames {}".format( plug["denoiseNeighborFrames"]["value"].getValue() ) )

	if plug["denoiseClampInput"]["enabled"].getValue() :
		info.append( "Clamp Input {}".format( plug["denoiseClampInput"]["value"].getValue() ) )

	return ", ".join( info )

def __curvesSummary( plug ) :

	info = []

	if plug["useCurves"]["enabled"].getValue() :
		info.append( "Use Curves {}".format( plug["useCurves"]["value"].getValue() ) )

	if plug["curveMinimumWidth"]["enabled"].getValue() :
		info.append( "Minimum Width {}".format( plug["curveMinimumWidth"]["value"].getValue() ) )

	if plug["curveMaximumWidth"]["enabled"].getValue() :
		info.append( "Maximum Width {}".format( plug["curveMaximumWidth"]["value"].getValue() ) )

	if plug["curvePrimitive"]["enabled"].getValue() :
		info.append( "Primitive {}".format( plug["curvePrimitive"]["value"].getValue() ) )

	if plug["curveShape"]["enabled"].getValue() :
		info.append( "Shape {}".format( plug["curveShape"]["value"].getValue() ) )

	if plug["curveResolution"]["enabled"].getValue() :
		info.append( "Resolution {}".format( plug["curveResolution"]["value"].getValue() ) )

	if plug["curveSubdivisions"]["enabled"].getValue() :
		info.append( "Subdivisions {}".format( plug["curveSubdivisions"]["value"].getValue() ) )

	if plug["curveCullBackfacing"]["enabled"].getValue() :
		info.append( "Cull Backfacing {}".format( plug["curveCullBackfacing"]["value"].getValue() ) )

	return ", ".join( info )

def __backgroundSummary( plug ) :

	info = []

	if plug["aoFactor"]["enabled"].getValue() :
		info.append( "AO Factor {}".format( plug["aoFactor"]["value"].getValue() ) )

	if plug["aoDistance"]["enabled"].getValue() :
		info.append( "AO Distance {}".format( plug["aoDistance"]["value"].getValue() ) )

	if plug["bgUseShader"]["enabled"].getValue() :
		info.append( "Use Shader {}".format( plug["bgUseShader"]["value"].getValue() ) )

	if plug["useAO"]["enabled"].getValue() :
		info.append( "Use AO {}".format( plug["useAO"]["value"].getValue() ) )

	if plug["bgTransparent"]["enabled"].getValue() :
		info.append( "Transparent {}".format( plug["bgTransparent"]["value"].getValue() ) )

	if plug["bgTransparentGlass"]["enabled"].getValue() :
		info.append( "Transparent Glass {}".format( plug["bgTransparentGlass"]["value"].getValue() ) )

	if plug["bgTransparentRoughnessThreshold"]["enabled"].getValue() :
		info.append( "Roughness Threshold {}".format( plug["bgTransparentRoughnessThreshold"]["value"].getValue() ) )

	for childName in ( "Camera", "Diffuse", "Glossy", "Transmission", "Shadow", "Scatter" ) :
		if plug["bg" + childName + "Visibility"]["enabled"].getValue() :
			info.append( IECore.CamelCase.toSpaced( childName ) + ( " On" if plug["bg" + childName + "Visibility"]["value"].getValue() else " Off" ) )

	return ", ".join( info )

def __devicePresetNames( plug ) :

	presetNames = IECore.StringVectorData()

	for device in GafferCycles.devices :
		presetNames.append( "%s - %s" % ( device["type"], device["description"] ) )

	return presetNames

def __devicePresetValues( plug ) :

	presetValues = IECore.StringVectorData()

	for device in GafferCycles.devices :
		presetValues.append( device["id"] )

	return presetValues

Gaffer.Metadata.registerNode(

	GafferCycles.CyclesOptions,

	"description",
	"""
	Sets global scene options applicable to the Cycles
	renderer. Use the StandardOptions node to set
	global options applicable to all renderers.
	""",

	plugs = {

		# Sections

		"options" : [

			"layout:section:Session:summary", __sessionSummary,
			"layout:section:Scene:summary", __sceneSummary,
			"layout:section:Sampling:summary", __samplingSummary,
			"layout:section:Ray Depth:summary", __rayDepthSummary,
			"layout:section:Volumes:summary", __volumesSummary,
			"layout:section:Caustics:summary", __causticsSummary,
			"layout:section:Subdivision:summary", __subdivisionSummary,
			"layout:section:Film:summary", __filmSummary,
			"layout:section:Denoising:summary", __denoisingSummary,
			"layout:section:Curves:summary", __curvesSummary,
			"layout:section:Background:summary", __backgroundSummary,

		],

		# Session

		"options.device" : [

			"description",
			"""
			Device to use for rendering.
			""",

			"layout:section", "Session",
			"label", "Device",

		],

		"options.device.value" : [

		"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",
		"presetNames", __devicePresetNames,
		"presetValues", __devicePresetValues,

		],

		"options.featureSet" : [

			"description",
			"""
			Feature set to use for rendering.
			- Supported : Only use finished and supported features
			- Experimental : Use experimental and incomplete features
								that might be broken or change in the 
								future.
			""",

			"layout:section", "Session",

		],

		"options.featureSet.value" : [

			"preset:Supported", False,
			"preset:Experimental", True,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.shadingSystem" : [

			"description",
			"""
			Shading system.

			- OSL : Use Open Shading Language (CPU rendering only).
			- SVM : Use Shader Virtual Machine.
			""",

			"layout:section", "Session",

		],

		"options.shadingSystem.value" : [

			"preset:OSL", "OSL",
			"preset:SVM", "SVM",

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.numThreads" : [

			"description",
			"""
			The number of threads used for rendering.

			- The default value of 0 lets the renderer choose
				an optimal number of threads based on the available
				hardware.
			- Positive values directly set the number of threads.
			- Negative values can be used to reserve some cores
				while otherwise letting the renderer choose the
				optimal number of threads.
			""",

			"layout:section", "Session",

		],

		"options.tileOrder" : [

			"description",
			"""
			Tile order for rendering.
			""",

			"layout:section", "Session",

		],

		"options.tileOrder.value" : [

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",
			"presetNames", IECore.StringVectorData( ["Center", "Right to Left", "Left to Right", "Top to Bottom", "Bottom to Top", "Hilbert Spiral"] ),
			"presetValues", IECore.IntVectorData( [0, 1, 2, 3, 4, 5] ),

		],

		"options.tileSize" : [

			"description",
			"""
			Tile size for rendering.
			""",

			"layout:section", "Session",

		],

		"options.startResolution" : [

			"description",
			"""
			Start resolution.
			""",

			"layout:section", "Session",

		],

		"options.pixelSize" : [

			"description",
			"""
			Pixel Size.
			""",

			"layout:section", "Session",

		],

		"options.cancelTimeout" : [

			"description",
			"""
			Cancel Timeout.
			""",

			"layout:section", "Session",

		],

		"options.resetTimeout" : [

			"description",
			"""
			Reset Timeout.
			""",

			"layout:section", "Session",

		],

		"options.textTimeout" : [

			"description",
			"""
			Text Timeout.
			""",

			"layout:section", "Session",

		],

		"options.progressiveUpdateTimeout" : [

			"description",
			"""
			Progressive Update Timeout.
			""",

			"layout:section", "Session",

		],

		# Scene

		"options.bvhLayout" : [

			"description",
			"""
			BVH Layout size. This corresponds with CPU architecture
			(the higher the faster, but might not be supported on old CPUs).
			""",

			"layout:section", "Scene",
			"label", "BVH Layout",

		],

		"options.bvhLayout.value" : [

			"preset:BVH2", 0 | ( 1 << 0 ),
			"preset:BVH4", 0 | ( 1 << 1 ),
			"preset:BVH8", 0 | ( 1 << 2 ),
			"preset:EMBREE", 0 | ( 1 << 3 ),

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.useBvhSpatialSplit" : [

			"description",
			"""
			Use BVH spatial splits: longer builder time, faster render.
			""",

			"layout:section", "Scene",
			"label", "Use Spatial Splits",

		],

		"options.useBvhUnalignedNodes" : [

			"description",
			"""
			Use special type BVH optimized for hair (uses more ram but renders faster).
			""",

			"layout:section", "Scene",
			"label", "Use Hair BVH",

		],

		"options.numBvhTimeSteps" : [

			"description",
			"""
			Split BVH primitives by this number of time steps to speed up render time in cost of memory.
			""",

			"layout:section", "Scene",
			"label", "BVH Time Steps",

		],

		"options.textureLimit" : [

			"description",
			"""
			Limit the maximum texture size used by final rendering.
			""",

			"layout:section", "Scene",
			"label", "Texture Size Limit",

		],

		"options.textureLimit.value" : [

			"preset:No Limit", 0,
			"preset:128", 1,
			"preset:256", 2,
			"preset:512", 3,
			"preset:1024", 4,
			"preset:2048", 5,
			"preset:4096", 6,
			"preset:8192", 7,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		# Sampling

		"options.method" : [

			"description",
			"""
			Method to sample lights and materials.

			- Branched Path : Path tracing integrator that branches on
			  the first bounce, giving more control over the number of
			  light and material samples.
			- Path Tracing : Pure path tracing integrator.
			""",

			"layout:section", "Sampling",
			"label", "Integrator",

		],

		"options.method.value" : [

			"preset:BranchedPath", False,
			"preset:Path", True,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.samples" : [

			"description",
			"""
			Number of samples to render for each pixel. This is for the
			path integrator, use the other sampling parameters for the 
			branched-path integrator.
			""",

			"layout:section", "Sampling",
			"label", "Samples",

		],

		"options.aaSamples" : [

			"description",
			"""
			The number of antialiasing samples to render for 
			each pixel.
			""",

			"layout:section", "Sampling",
			"label", "AntiAlias",

		],

		"options.diffuseSamples" : [

			"description",
			"""
			Number of diffuse bounce samples to render for each 
			AA sample.
			""",

			"layout:section", "Sampling",
			"label", "Diffuse",

		],

		"options.glossySamples" : [

			"description",
			"""
			Number of glossy bounce samples to render for each 
			AA sample.
			""",

			"layout:section", "Sampling",
			"label", "Glossy",

		],

		"options.transmissionSamples" : [

			"description",
			"""
			Number of transmission bounce samples to render for 
			each AA sample.
			""",

			"layout:section", "Sampling",
			"label", "Transmission",

		],

		"options.aoSamples" : [

			"description",
			"""
			Number of ambient occlusion bounce samples to render
			for each AA sample.
			""",

			"layout:section", "Sampling",
			"label", "Ambient Occlusion",

		],

		"options.meshlightSamples" : [

			"description",
			"""
			Number of mesh emission light bounce samples to render
			for each AA sample.
			""",

			"layout:section", "Sampling",
			"label", "Meshlight",

		],

		"options.subsurfaceSamples" : [

			"description",
			"""
			Number of subsurface scattering samples to render for each 
			AA sample.
			""",

			"layout:section", "Sampling",
			"label", "Subsurface",

		],

		"options.volumeSamples" : [

			"description",
			"""
			Number of volume scattering samples to render for each AA sample.
			""",

			"layout:section", "Sampling",

		],

		"options.samplingPattern" : [

			"description",
			"""
			Random sampling pattern used by the integrator.
			""",

			"layout:section", "Sampling",

		],

		"options.samplingPattern.value" : [

			"preset:Sobol", 0,
			"preset:Correlated Multi-Jitter", 1,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.sampleAllLightsDirect" : [

			"description",
			"""
			Sample all lights (for direct samples), rather than randomly picking one.
			""",

			"layout:section", "Sampling",

		],

		"options.sampleAllLightsIndirect" : [

			"description",
			"""
			Sample all lights (for indirect samples), rather than randomly picking one.
			""",

			"layout:section", "Sampling",

		],

		"options.lightSamplingThreshold" : [

			"description",
			"""
			Probabilistically terminate light samples when the light
			contribution is below this threshold (more noise but faster
			rendering). "
            "Zero disables the test and never ignores lights.
			""",

			"layout:section", "Sampling",

		],

		"options.filterGlossy" : [

			"description",
			"""
			Adaptively blur glossy shaders after blurry bounces, to reduce
			noise at the cost of accuracy.
			""",

			"layout:section", "Sampling",

		],

		"options.seed" : [

			"description",
			"""
			Seed value for the sampling pattern.
			""",

			"layout:section", "Sampling",
			"label", "Seed Value",

		],

		"options.sampleClampDirect" : [

			"description",
			"""
			Clamp value for sampling direct rays.
			""",

			"layout:section", "Sampling",

		],

		"options.sampleClampIndirect" : [

			"description",
			"""
			Clamp value for sampling indirect rays.
			""",

			"layout:section", "Sampling",

		],

		"options.startSample" : [

			"description",
			"""
			Start sample.
			""",

			"layout:section", "Sampling",

		],

		# Ray Depth

		"options.maxBounce" : [

			"description",
			"""
			Total maximum number of bounces.
			""",

			"layout:section", "Ray Depth",
			"label", "Max Bounces",

		],

		"options.maxDiffuseBounce" : [

			"description",
			"""
			Maximum number of diffuse reflection bounces, bounded by total
			maximum.
			""",

			"layout:section", "Ray Depth",
			"label", "Diffuse",

		],

		"options.maxGlossyBounce" : [

			"description",
			"""
			Maximum number of glossy reflection bounces, bounded by total
			maximum.
			""",

			"layout:section", "Ray Depth",
			"label", "Glossy",

		],

		"options.maxTransmissionBounce" : [

			"description",
			"""
			Maximum number of transmission reflection bounces, bounded by total
			maximum.
			""",

			"layout:section", "Ray Depth",
			"label", "Transmission",

		],

		"options.maxVolumeBounce" : [

			"description",
			"""
			Maximum number of volumetric scattering events.
			""",

			"layout:section", "Ray Depth",
			"label", "Volume",

		],

		"options.transparentMaxBounce" : [

			"description",
			"""
			Maximum number of transparent bounces.
			""",

			"layout:section", "Ray Depth",
			"label", "Transparency",

		],

		"options.aoBounces" : [

			"description",
			"""
			Maximum number of Ambient Occlusion bounces.
			""",

			"layout:section", "Ray Depth",
			"label", "Ambient Occlusion",

		],

		# Volumes

		"options.volumeStepSize" : [

			"description",
			"""
			Distance between volume shader samples when rendering the volume
            (lower values give more accurate and detailed results, but also
			increases render time).
			""",

			"layout:section", "Volumes",

		],

		"options.volumeMaxSteps" : [

			"description",
			"""
			Maximum number of steps through the volume before giving up,
            to avoid extremely long render times with big objects or small step
			sizes.
			""",

			"layout:section", "Volumes",

		],

		# Caustics

		"options.causticsReflective" : [

			"description",
			"""
			Use reflective caustics, resulting in a brighter image 
			(more noise but added realism).
			""",

			"layout:section", "Caustics",
			"label", "Reflective Caustics",

		],

		"options.causticsRefractive" : [

			"description",
			"""
			Use refractive caustics, resulting in a brighter image 
			(more noise but added realism).
			""",

			"layout:section", "Caustics",
			"label", "Refractive Caustics",

		],

		# Subdivision

		"options.dicingRate" : [

			"description",
			"""
			Size of a micropolygon in pixels.
			""",

			"layout:section", "Subdivision",

		],

		"options.maxSubdivisions" : [

			"description",
			"""
			Stop subdividing when this level is reached even if the dice rate
			would produce finer tessellation.
			""",

			"layout:section", "Subdivision",

		],

		"options.dicingCamera" : [

			"description",
			"""
			Camera to use as reference point when subdividing geometry, useful
			to avoid crawling artifacts in animations when the scene camera is
			moving.
			""",

			"layout:section", "Subdivision",

		],

		"options.offscreenDicingScale" : [

			"description",
			"""
			Multiplier for dicing rate of geometry outside of the camera view. 
			The dicing rate of objects is gradually increased the further they 
			are outside the camera view. Lower values provide higher quality 
			reflections and shadows for off screen objects, while higher values
			use less memory.
			""",

			"layout:section", "Subdivision",

		],

		# Background

		"options.aoFactor" : [

			"description",
			"""
			Ambient Occlusion factor.
			""",

			"layout:section", "Background",
			"label", "Ambient Occlusion Factor",

		],

		"options.aoDistance" : [

			"description",
			"""
			Ambient Occlusion Distance.
			""",

			"layout:section", "Background",
			"label", "Ambient Occlusion Distance",

		],

		"options.bgUseShader" : [

			"description",
			"""
			Use background shader. There must be a CyclesBackground node with
			a shader attached to it.
			""",

			"layout:section", "Background",
			"label", "Use Shader",

		],

		"options.useAO" : [

			"description",
			"""
			Enable Ambient Occlusion.
			""",

			"layout:section", "Background",
			"label", "Use Ambient Occlusion",

		],

		"options.bgTransparent" : [

			"description",
			"""
			Make the background transparent.
			""",

			"layout:section", "Background",
			"label", "Transparent",

		],

		"options.bgTransparentGlass" : [

			"description",
			"""
			Background can be seen through transmissive surfaces.
			""",

			"layout:section", "Background",
			"label", "Transmission Visible",

		],

		"options.bgTransparentRoughnessThreshold" : [

			"description",
			"""
			Roughness threshold of background shader in transmissive surfaces.
			""",

			"layout:section", "Background",
			"label", "Roughness Threshold",

		],

		# BG Visibility

		"options.bgCameraVisibility" : [

			"description",
			"""
			Whether or not the background is visible to camera
			rays.
			""",

			"layout:section", "Background",
			"label", "Camera Visible",

		],

		"options.bgDiffuseVisibility" : [

			"description",
			"""
			Whether or not the background is visible to diffuse
			rays.
			""",

			"layout:section", "Background",
			"label", "Diffuse Visible",

		],

		"options.bgGlossyVisibility" : [

			"description",
			"""
			Whether or not the background is visible in
			glossy rays.
			""",

			"layout:section", "Background",
			"label", "Glossy Visible",

		],

		"options.bgTransmissionVisibility" : [

			"description",
			"""
			Whether or not the background is visible in
			transmission.
			""",

			"layout:section", "Background",
			"label", "Transmission Visible",

		],

		"options.bgShadowVisibility" : [

			"description",
			"""
			Whether or not the background is visible to shadow
			rays - whether it casts shadows or not.
			""",

			"layout:section", "Background",
			"label", "Shadow Visible",

		],

		"options.bgScatterVisibility" : [

			"description",
			"""
			Whether or not the background is visible to
			scatter rays.
			""",

			"layout:section", "Background",
			"label", "Scatter Visible",

		],

		# Film

		"options.exposure" : [

			"description",
			"""
			Image brightness scale.
			""",

			"layout:section", "Film",

		],

		"options.passAlphaThreshold" : [

			"description",
			"""
			Alpha threshold.
			""",

			"layout:section", "Film",

		],

		"options.filterType" : [

			"description",
			"""
			Image filter type.
			""",

			"layout:section", "Film",

		],

		"options.filterType.value" : [

			"preset:Box", 0,
			"preset:Gaussian", 1,
			"preset:Blackman Harris", 2,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.filterWidth" : [

			"description",
			"""
			Pixel width of the filter.
			""",

			"layout:section", "Film",

		],

		"options.mistStart" : [

			"description",
			"""
			Start of the mist/fog.
			""",

			"layout:section", "Film",

		],

		"options.mistDepth" : [

			"description",
			"""
			End of the mist/fog.
			""",

			"layout:section", "Film",

		],

		"options.mistFalloff" : [

			"description",
			"""
			Falloff of the mist/fog.
			""",

			"layout:section", "Film",

		],

		"options.useSampleClamp" : [

			"description",
			"""
			Use sample clamp.
			""",

			"layout:section", "Film",

		],

		"options.denoisingDataPass" : [

			"description",
			"""
			Denoising data pass.
			""",

			"layout:section", "Film",

		],

		"options.denoisingCleanPass" : [

			"description",
			"""
			Denoising clean pass.
			""",

			"layout:section", "Film",

		],

		# Denoising

		"options.runDenoising" : [

			"description",
			"""
			Denoise the rendered image. This is Cycles' built-in denoising.
			""",

			"layout:section", "Denoising",
			"label", "Run Denoising",

		],

		"options.writeDenoisingPasses" : [

			"description",
			"""
			Write the denoising passes.
			""",

			"layout:section", "Denoising",
			"label", "Write Denoising Passes",

		],

		"options.fullDenoising" : [

			"description",
			"""
			Full Denoising.
			""",

			"layout:section", "Denoising",
			"label", "Full Denoising",

		],

		"options.denoisingDiffuseDirect" : [

			"description",
			"""
			Denoise the direct diffuse lighting.
			""",

			"layout:section", "Denoising",
			"label", "Diffuse Direct",

		],

		"options.denoisingDiffuseIndirect" : [

			"description",
			"""
			Denoise the indirect diffuse lighting.
			""",

			"layout:section", "Denoising",
			"label", "Diffuse Indirect",

		],

		"options.denoisingGlossyDirect" : [

			"description",
			"""
			Denoise the direct glossy lighting.
			""",

			"layout:section", "Denoising",
			"label", "Glossy Direct",

		],

		"options.denoisingGlossyIndirect" : [

			"description",
			"""
			Denoise the indirect glossy lighting.
			""",

			"layout:section", "Denoising",
			"label", "Glossy Indirect",

		],

		"options.denoisingTransmissionDirect" : [

			"description",
			"""
			Denoise the direct transmission lighting.
			""",

			"layout:section", "Denoising",
			"label", "Transmission Direct",

		],

		"options.denoisingTransmissionIndirect" : [

			"description",
			"""
			Denoise the indirect transmission lighting.
			""",

			"layout:section", "Denoising",
			"label", "Transmission Indirect",

		],

		"options.denoisingSubsurfaceDirect" : [

			"description",
			"""
			Denoise the direct subsurface lighting.
			""",

			"layout:section", "Denoising",
			"label", "Subsurface Direct",

		],

		"options.denoisingSubsurfaceIndirect" : [

			"description",
			"""
			Denoise the indirect subsurface lighting.
			""",

			"layout:section", "Denoising",
			"label", "Subsurface Indirect",

		],

		"options.denoiseStrength" : [

			"description",
			"""
			Controls neighbor pixel weighting for the denoising filter
			(lower values preserve more detail, but aren't as smooth).
			""",

			"layout:section", "Denoising",
			"label", "Denoise Strength",

		],

		"options.denoiseFeatureStrength" : [

			"description",
			"""
			Controls removal of noisy image feature passes 
			(lower values preserve more detail, but aren't as smooth).
			""",

			"layout:section", "Denoising",
			"label", "Denoise Feature Strength",

		],

		"options.denoiseRadius" : [

			"description",
			"""
			Size of the image area that's used to denoise a pixel 
			(higher values are smoother, but might lose detail and are slower).
			""",

			"layout:section", "Denoising",
			"label", "Denoise Radius",

		],

		"options.denoiseRelativePca" : [

			"description",
			"""
			When removing pixels that don't carry information, use a relative
			threshold instead of an absolute one (can help to reduce artifacts,
			but might cause detail loss around edges).
			""",

			"layout:section", "Denoising",
			"label", "Denoise Relative Filter",

		],

		"options.denoiseNeighborFrames" : [
		
			"description",
			"""
			Number of frames to use around the current frame for denoising.
			""",
		
			"layout:section", "Denoising",
			"label", "Denoise Neighbor Frames",
		
		],

		"options.denoiseNeighborFrames" : [
		
			"description",
			"""
			Number of frames to use around the current frame for denoising.
			""",
		
			"layout:section", "Denoising",
			"label", "Denoise Neighbor Frames",
		
		],

		"options.denoiseClampInput" : [
		
			"description",
			"""
			Denoise Clamp Input.
			""",
		
			"layout:section", "Denoising",
			"label", "Denoise Clamp Input",
		
		],

		# Curves

		"options.useCurves" : [

			"description",
			"""
			Activate Cycles curves/hair particle system.
			""",

			"layout:section", "Curves",
			"label", "Enable Curve Particles",

		],

		"options.curveMinimumWidth" : [

			"description",
			"""
			Minimal pixel width for strand (0 - deactivated).
			""",

			"layout:section", "Curves",
			"label", "Minimum Width",

		],

		"options.curveMaximumWidth" : [

			"description",
			"""
			Maximum extension that strand radius can be increased by.
			""",

			"layout:section", "Curves",
			"label", "Minimum Width",

		],

		"options.curvePrimitive" : [

			"description",
			"""
			Curve primitve type.
			""",

			"layout:section", "Curves",
			"label", "Primitive",

		],

		"options.curvePrimitive.value" : [

			"preset:Triangles", 0,
			"preset:LineSegments", 1,
			"preset:Segments", 2,
			"preset:Ribbons", 3,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.curveShape" : [

			"description",
			"""
			Curve shape type.
			""",

			"layout:section", "Curves",
			"label", "Shape",

		],

		"options.curveShape.value" : [

			"preset:Ribbon", 0,
			"preset:Thick", 1,

			"plugValueWidget:type", "GafferUI.PresetsPlugValueWidget",

		],

		"options.curveResolution" : [

			"description",
			"""
			Curve resolution.
			""",

			"layout:section", "Curves",
			"label", "Resolution",

		],

		"options.curveSubdivisions" : [

			"description",
			"""
			Curve subdivisions.
			""",

			"layout:section", "Curves",
			"label", "Subdivisions",

		],

		"options.curveCullBackfacing" : [

			"description",
			"""
			Curve cull back-faces.
			""",

			"layout:section", "Curves",
			"label", "CullBackfacing",

		],
	}
)
