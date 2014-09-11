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
		#layout.operator("copy_rigid_body_settings.copy_to_all_in_group", text = "Copy to Group Members")
		
		
# operators
###################################
		
class NewSettingsGroup(bpy.types.Operator):
	bl_idname = "copy_rigid_body_settings.create_settings_group"
	bl_label = "New Rigid Body Settings Group"
	bl_description = "Create a group from selected objects."
	
	def execute(self, context):
		group = newGroup(groupPrefix)
		return{"FINISHED"}
		
	
	
# register
##################################

def register():
	bpy.utils.register_module(__name__)

def unregister():
	bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
	register()