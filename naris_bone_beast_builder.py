"""
CALL OF NARIS — Bone Beast Builder (Blender Python)
------------------------------------------------------------------
يبني block-out لوحش العظام (Bone Beast - NARIS-ENM-W04-0004)
بتشريح عظمي متفحم، عيون عنبرية متعددة، توهج سماوي في الفجوات،
ونواة بنفسجية في الصدر.

الاستخدام:
    1. افتح Blender
    2. اذهب إلى Scripting Tab
    3. افتح هذا الملف أو الصقه
    4. اضغط Run Script (Alt+P)
"""

import bpy
import math

beast_collection = bpy.data.collections.new("NARIS_BoneBeast")
bpy.context.scene.collection.children.link(beast_collection)


def move_to_collection(obj, coll):
    for c in obj.users_collection:
        c.objects.unlink(obj)
    coll.objects.link(obj)


# ==================== المواد ====================

def make_bone_material(name="NARIS_BoneHide"):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nodes, links = nt.nodes, nt.links
    nodes.clear()

    output = nodes.new("ShaderNodeOutputMaterial")
    output.location = (500, 0)

    bsdf = nodes.new("ShaderNodeBsdfPrincipled")
    bsdf.location = (150, 0)
    bsdf.inputs["Base Color"].default_value = (0.25, 0.22, 0.18, 1.0)  # عظم متفحم رمادي داكن
    bsdf.inputs["Roughness"].default_value = 0.8

    # توهج سماوي خفيف في الحواف
    fresnel = nodes.new("ShaderNodeFresnel")
    fresnel.location = (-150, -200)

    emission = nodes.new("ShaderNodeEmission")
    emission.location = (-150, -300)
    emission.inputs["Color"].default_value = (0.0, 0.6, 1.0, 1.0)  # Cyan
    emission.inputs["Strength"].default_value = 0.8

    mix = nodes.new("ShaderNodeMixShader")
    mix.location = (250, -150)
    links.new(fresnel.outputs["Fac"], mix.inputs[0])
    links.new(bsdf.outputs["BSDF"], mix.inputs[1])
    links.new(emission.outputs["Emission"], mix.inputs[2])
    links.new(mix.outputs["Shader"], output.inputs["Surface"])

    return mat


def make_eye_material(name="NARIS_BoneEye", color=(1.0, 0.6, 0.0), strength=20.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nodes, links = nt.nodes, nt.links
    nodes.clear()

    output = nodes.new("ShaderNodeOutputMaterial")
    output.location = (300, 0)

    emission = nodes.new("ShaderNodeEmission")
    emission.location = (0, 0)
    emission.inputs["Color"].default_value = (*color, 1.0)
    emission.inputs["Strength"].default_value = strength

    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return mat


def make_core_material(name="NARIS_VioletCore", color=(0.48, 0.18, 0.55), strength=15.0):
    mat = bpy.data.materials.new(name)
    mat.use_nodes = True
    nt = mat.node_tree
    nodes, links = nt.nodes, nt.links
    nodes.clear()

    output = nodes.new("ShaderNodeOutputMaterial")
    output.location = (300, 0)

    emission = nodes.new("ShaderNodeEmission")
    emission.location = (0, 0)
    emission.inputs["Color"].default_value = (*color, 1.0)
    emission.inputs["Strength"].default_value = strength

    links.new(emission.outputs["Emission"], output.inputs["Surface"])
    return mat


bone_mat = make_bone_material()
eye_mat = make_eye_material()
core_mat = make_core_material()


# ==================== أداة بناء الأجزاء ====================

def add_part(name, shape, location, dimensions, rotation=(0, 0, 0), material=None, bevel_width=0.05):
    if shape == 'CUBE':
        bpy.ops.mesh.primitive_cube_add(location=location)
    elif shape == 'SPHERE':
        bpy.ops.mesh.primitive_uv_sphere_add(location=location, segments=28, ring_count=18)
    elif shape == 'CYLINDER':
        bpy.ops.mesh.primitive_cylinder_add(location=location, vertices=12)
    elif shape == 'CONE':
        bpy.ops.mesh.primitive_cone_add(location=location, vertices=4)
    elif shape == 'TORUS':
        bpy.ops.mesh.primitive_torus_add(location=location, major_segments=24, minor_segments=12)

    obj = bpy.context.active_object
    obj.name = name

    if shape != 'TORUS':
        obj.dimensions = dimensions
    else:
        obj.scale = (dimensions[0], dimensions[1], dimensions[2])

    obj.rotation_euler = tuple(math.radians(r) for r in rotation)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    if bevel_width > 0:
        bevel = obj.modifiers.new("Soften", type='BEVEL')
        bevel.width = bevel_width
        bevel.segments = 3

    if material:
        obj.data.materials.append(material)

    return obj


# ==================== بناء الهيكل العظمي ====================

Y_POS = -45.0  # بعيد في الأفق

# العمود الفقري
spine = add_part("Beast_Spine", 'CYLINDER', (0, Y_POS, 5), (1.5, 1.5, 8),
                  rotation=(90, 0, 0), material=bone_mat)

# القفص الصدري (عظام ملتوية)
for i in range(1, 6):
    add_part(f"Beast_Rib_{i}", 'TORUS', (0, Y_POS + 2.5 - i, 6.0), (1.2, 1.2, 1.2),
              rotation=(90, 0, 0), material=bone_mat)

# الجمجمة
skull = add_part("Beast_Skull", 'CUBE', (0, Y_POS - 5.5, 6.5), (2.5, 3.5, 2.5),
                  rotation=(15, 0, 0), material=bone_mat)
jaw = add_part("Beast_Jaw", 'CUBE', (0, Y_POS - 7.5, 5.5), (2.0, 2.5, 1.0),
               rotation=(25, 0, 0), material=bone_mat)

# الأطراف (عظام ضخمة)
leg_l = add_part("Beast_Leg_L", 'CYLINDER', (-3.5, Y_POS, 2.5), (0.8, 0.8, 5), material=bone_mat)
leg_r = add_part("Beast_Leg_R", 'CYLINDER', (3.5, Y_POS, 2.5), (0.8, 0.8, 5), material=bone_mat)

# العيون العنبرية المتعددة
eye_positions = [[-0.4, -0.1], [0.0, -0.2], [0.4, -0.1], [-0.2, -0.4], [0.2, -0.4]]
for i, ep in enumerate(eye_positions):
    add_part(f"Beast_Eye_{i}", 'SPHERE', (ep[0], Y_POS - 6.5, 6.5 + ep[1]), (0.25, 0.25, 0.25),
              material=eye_mat, bevel_width=0.0)

# النواة البنفسجية في الصدر
core = add_part("Beast_Core", 'SPHERE', (0, Y_POS + 2.0, 7.0), (0.8, 0.8, 0.8),
                 material=core_mat, bevel_width=0.0)

# ==================== التجميع ====================

all_parts = [spine, skull, jaw, leg_l, leg_r, core]
for i in range(1, 6):
    all_parts.append(bpy.data.objects[f"Beast_Rib_{i}"])
for i in range(5):
    all_parts.append(bpy.data.objects[f"Beast_Eye_{i}"])

for obj in all_parts:
    move_to_collection(obj, beast_collection)

# ==================== إضاءة النواة ====================

light_data = bpy.data.lights.new("Light_BeastCore", type='POINT')
light_data.energy = 2000.0
light_data.color = (0.48, 0.18, 0.55)
light_obj = bpy.data.objects.new("Light_BeastCore", light_data)
light_obj.location = (0, Y_POS + 2.0, 7.0)
bpy.context.scene.collection.objects.link(light_obj)
move_to_collection(light_obj, beast_collection)

print("Bone Beast block-out built successfully (NARIS-ENM-W04-0004).")
