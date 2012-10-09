import bpy, bgl, blf,sys 
from bpy import data, ops, props, types, context

print("Usage: blender -b template.blend -P tile-render.py -- [zooming=1] [out=e:/tmp/] file=file.blend")

zooming = 1
scene = bpy.data.scenes[bpy.data.scenes.keys()[0]]
baseX = scene.render.resolution_x;
baseY = scene.render.resolution_y;
file = ""
out = "e:/tmp/"

for arg in sys.argv: 
	words = arg.split('=') 
	if (words[0] == 'zooming'): 
		zooming = int(words[1])
	
	if (words[0] == 'out'):
		out = words[1]
	
	if (words[0] == 'file'):
		file = words[1].split('.')[0]

filepath = file + '.blend'

print("Loading " + filepath + "...")

with bpy.data.libraries.load(filepath) as (data_from, lib):
	lib.objects = [name for name in data_from.objects]

for obj in lib.objects:
	print("Appending " + obj.name + "...")
	scene.objects.link(obj)
			
for mul in range(1, zooming+1):
	scene.render.resolution_x = baseX * mul
	scene.render.resolution_y = baseY * mul
	scene.render.filepath = out + file + "_" + str(baseX * mul) + "x" + str(baseY * mul)
	print("Rendering " + scene.render.filepath + "...")
	bpy.ops.render.render( write_still=True )