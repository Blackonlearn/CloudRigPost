import bpy
from rigify.feature_sets import CloudRig
post_generation_utils = CloudRig.rigs.sprite_fright.post_generation_utils
rig = bpy.context.object

post_generation_utils.add_ui_data(rig, "Facial Settings", 'Mouth Lock'
    ,info = {
        'prop_bone' : 'MyCustomProperties',
        'prop_id' : 'Mouth Lock',
        'texts' : '["Unlocked", "Locked"]',
        'operator' : 'pose.cloudrig_snap_bake'
        'bones' : ['STR-FannyPack1', 'STR-FannyPack2', 'STR-FannyPack3', 'STR-FannyPack4', 'STR-FannyPack5', 'STR-TIP-FannyPack5', 'STR-FannyPack7']
    }
    ,default = 0, max=1
    ,label_name = "Mouth Lock"
)

for txt in ['cloudrig.py']:
    tdb = bpy.data.texts[txt]
    tdb.make_local()
    tdb.filepath = ""
    
    
    
#MISC
post_generation_utils.add_ui_data(rig, "Clothes", 'Fanny Pack'
    ,info = {
        'prop_bone' : 'PRP-Spine',
        'prop_id' : 'Fanny Pack',
        'texts' : '["Attached", "Detached", "Hidden"]',
        'operator' : 'pose.cloudrig_snap_bake',
        'bones' : ['STR-FannyPack1', 'STR-FannyPack2', 'STR-FannyPack3', 'STR-FannyPack4', 'STR-FannyPack5', 'STR-TIP-FannyPack5', 'STR-FannyPack7']
    }
    ,default = 0, max=2
    ,label_name = "Fannypack"
)
post_generation_utils.add_ui_data(rig, 'Clothes', 'LongStrap'
    ,info = {
        'prop_bone' : 'PRP-Spine',
        'prop_id' : 'FannyPackStrap',
    }
    ,default = 0
    ,label_name = "Fannypack"
    ,entry_name = "Long Strap"
)
post_generation_utils.add_ui_data(rig, 'ce', 'Line 1'
    ,info = {
        'prop_bone' : 'PRP-Head',
        'prop_id' : 'Face Line 1',
    }
    ,default = 0
    ,label_name = "Lines"
)
post_generation_utils.add_ui_data(rig, 'ce', 'Line 1'
    ,info = {
        'prop_bone' : 'PRP-Head',
        'prop_id' : 'Face Line 2',
    }
    ,default = 0
    ,label_name = "Lines"
)
