import bpy
i = 1
startRatio = 1
finalRatio = 0.0001
numberOfFrames = 15
iterationValue = (finalRatio/startRatio)**(1/numberOfFrames)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
bpy.ops.import_scene.obj(filepath="Test.obj")
choiseofDecimate = 0
if(choiseofDecimate == 0):
    for obj in bpy.context.scene.objects:
        if(obj.type == 'MESH'):
            mesh = obj.data
            objectToSelect = bpy.data.objects[mesh.name]
            objectToSelect.select_set(True)
            bpy.context.view_layer.objects.active = objectToSelect
            x = int(len(mesh.polygons))
            print(x)
            while(x>5000):
                bpy.ops.object.modifier_add(type='DECIMATE')
                bpy.context.object.modifiers["Decimate"].use_collapse_triangulate = True
                bpy.context.object.modifiers["Decimate"].ratio = startRatio*(iterationValue**i)
                bpy.ops.object.modifier_apply(modifier="Decimate")
                x = int(len(mesh.polygons))
                i+=1
                print(x)
elif(choiseofDecimate == 1):
    for obj in bpy.context.scene.objects:
        if(obj.type == 'MESH'):
            mesh = obj.data
            x = int(len(mesh.polygons))
            print(x)
            while(x>250):
                bpy.ops.object.modifier_add(type='DECIMATE')
                bpy.context.object.modifiers["Decimate"].decimate_type = 'UNSUBDIV'
                bpy.context.object.modifiers["Decimate"].iterations = 1
                bpy.ops.object.modifier_apply(modifier="Decimate")
                x = int(len(mesh.polygons))
                print(x)

bpy.ops.export_scene.obj(filepath='Result.obj')



bpy.context.space_data.context = 'DATA'
bpy.context.object.data.remesh_voxel_size = 0.01
bpy.ops.object.voxel_remesh()
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.mark_sharp(clear=True)
bpy.ops.object.editmode_toggle()
bpy.ops.object.shade_smooth()