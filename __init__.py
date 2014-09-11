'''
Copyright (C) 2014 Jacques Lucke
mail@jlucke.com

Created by Jacques Lucke

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import bpy, sys, os
sys.path.append(os.path.dirname(__file__))
from copy_rigid_body_settings_utils import *

bl_info = {
	"name":        "Copy Rigid Body Settings",
	"description": "",
	"author":      "Jacques Lucke",
	"version":     (0, 0, 1),
	"blender":     (2, 7, 1),
	"location":    "View 3D > Tool Shelf",
	"category":    "3D View",
	"warning":	   "alpha"
	}
	
groupPrefix = "rigid body settings group"
	
	
	
def getLinkedObjects(object):
	objects = []
	groups = getGroupsWithPrefix(object, groupPrefix)
	for group in groups:
		objects.extend(getRigidBodyObjectsInGroup(group))
	return objects
					
def getRigidBodyObjectsInGroup(group):
	objects = []
	for object in group.objects:
		if object.rigid_body is not None: objects.append(object)
	return objects
	
def copyRigidBodySettings(source, target):
	target.angular_damping = source.angular_damping
	target.collision_groups = source.collision_groups
	target.collision_margin = source.collision_margin
	target.deactivate_angular_velocity = source.deactivate_angular_velocity
	target.deactivate_linear_velocity = source.deactivate_linear_velocity
	target.enabled = source.enabled
	target.friction = source.friction
	target.kinematic = source.kinematic
	target.linear_damping = source.linear_damping
	target.mass = source.mass
	target.mesh_source = source.mesh_source
	target.restitution = source.restitution
	target.type = source.type
	target.use_deactivation = source.use_deactivation
	target.use_deform = source.use_deform
	target.use_margin = source.use_margin
	target.use_start_deactivated = source.use_start_deactivated
	target.use_start_deactivated = source.use_start_deactivated

	
	
# interface
#############################

class CopyRigidBodySettingsPanel(bpy.types.Panel):
	bl_space_type = "VIEW_3D"
	bl_region_type = "TOOLS"
	bl_category = "Physics"
	bl_label = "Copy Rigid Body Settings"
	bl_context = "objectmode"
	
	@classmethod
	def poll(self, context):
		return context
	
	def draw(self, context):
		layout = self.layout
		
		layout.operator("copy_rigid_body_settings.create_settings_group", text = "New Settings Group")
		layout.operator("copy_rigid_body_settings.copy_to_all_in_group", text = "Copy to Settings Group")
		
		
# operators
###################################
		
class NewSettingsGroup(bpy.types.Operator):
	bl_idname = "copy_rigid_body_settings.create_settings_group"
	bl_label = "New Rigid Body Settings Group"
	bl_description = "Create a group from selected objects."
	
	def execute(self, context):
		group = newGroup(groupPrefix)
		selectedObjects = getSelectedObjects()
		for object in selectedObjects:
			group.objects.link(object)
		return{"FINISHED"}
		
class NewSettingsGroup(bpy.types.Operator):
	bl_idname = "copy_rigid_body_settings.copy_to_all_in_group"
	bl_label = "Copy Settings To Group Members"
	bl_description = "Copy settings from active object to all group members."
	
	def execute(self, context):
		activeObject = getActive()
		objects = getLinkedObjects(activeObject)
		for object in objects:
			copyRigidBodySettings(activeObject.rigid_body, object.rigid_body)
		return{"FINISHED"}
		
	
	
# register
##################################

def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()