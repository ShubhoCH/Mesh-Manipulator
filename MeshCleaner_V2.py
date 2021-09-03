import bpy
for obj in bpy.context.scene.objects:
    if(obj.type == 'MESH'):
        mesh = obj.data
        objectToSelect = bpy.data.objects[mesh.name]
        objectToSelect.select_set(True)
        bpy.context.view_layer.objects.active = objectToSelect
        bpy.context.space_data.context = 'DATA'
        bpy.context.object.data.remesh_voxel_size = 0.01
        bpy.ops.object.voxel_remesh()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.shade_smooth()