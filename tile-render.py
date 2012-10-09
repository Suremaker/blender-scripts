import bpy, bgl, blf,sys 
from bpy import data, ops, props, types, context

print("Usage: blender -b file.blend -P tile-render.py [zooming=1] [out=e:/tmp/]")

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
		
	words = arg.split('.')
	if (len(words) > 1 and words[1] == 'blend'):
		file = words[0]

for mul in range(1, zooming+1):
	scene.render.resolution_x = baseX * mul
	scene.render.resolution_y = baseY * mul
	scene.render.file_format = 'PNG'
	scene.render.filepath = out + file + "_" + str(baseX * mul) + "x" + str(baseY * mul)
	print("Rendering " + scene.render.filepath + "...")
	bpy.ops.render.render( write_still=True )