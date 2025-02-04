# NMSDK Changelog

## Releases:

### Current - v0.9.24

 - Fix exporting of texture filenames to always be upper case. [#90](https://github.com/monkeyman192/NMSDK/issues/90).

### Past:

### v0.9.23 (12/10/2022)

 - Many changes have been made to material handling on export:
   - Diffuse, Mask and Normal textures are now picked up from shader nodes and exported (and converted if need be)
   - These textures can be exported to either a local (within the context of an export) or shared texture directory.
 - A long standing bug was identified in the serialisation of geometry files which has been fixed.
 - Re-wrote export algorithm to match how the game works. This will be used in most cases except when the mesh being exported has complex uvs which result in islands. In this case the old method will be used since the uvs are not unique on vertexes.
 - MANY other various bug fixes and improvements.

### v0.9.22 (14/01/2021)

 - Added support for the `Capsule` primitive collision type. [#80](https://github.com/monkeyman192/NMSDK/issues/80).
 - Added support for loading and modifyin LOD values for scenes which have them. Those that do not cannot be modified currently. [#80](https://github.com/monkeyman192/NMSDK/issues/80).

### v0.9.21 (08/10/2020)

 - Vastly improved the system to allow importing scenes to be exported again. As part of this improvement a number of new API functions have been added as well as context menu items. Please see the [import page](importing/importing.md) for more details on usage. These changes have been across a fair chunk of the codebase, so I may have introduced some regressions, but this will be investigated more thoroughly in the next release.

### v0.9.20 (14/05/2020)

 - Release for Blender 2.82 (maybe 2.83? It is untested...). I don't think it will be compatible with 2.80 as I think there were some API changes between 2.80 and 2.82.
 - Fixed tests to be able to run better/easier.
 - Added an option to select the MBINCompiler.exe to use when importing/exporting scenes. If you have MBINCompiler registered to your path then this will be picked up automatically.
 - Fixed an issue where some scenes were unable to be imported due to a number of reasons [#64](https://github.com/monkeyman192/NMSDK/issues/64) and [#66](https://github.com/monkeyman192/NMSDK/issues/66).
 - Fixed a small bug [#62](https://github.com/monkeyman192/NMSDK/issues/62).
 - Collision node names are now shorter and more managable.

### v0.9.19 (01/11/2019)

This was a beta release for blender 2.80 update compatibility checking.
 - Added support for blender 2.80. Note that this plugin is **not** backward compatible, so it is not compatible with 2.79 as it is not worth the effort to make it compatible with both versions and maintain it.
 - Fixed some small bugs with the shader loading.

### v0.9.18  (13/10/2019)

 - Added the ability to import lighting. The current brightness setting is set at 1/100 of the value in the scene. This may change if better settings/node setup is found.
 - An option has been added to specify a custom location for the PCBANKS folder in case the scene file isn't located in the same folder as the unpacked data. The scene file *should* still line in a proper relative directory structure however.
 - The setting for indicating what the maximum number of animations has been changed. Now you can specify the value as a number, with `-1` being load all, `0` load none, and any positive number being the maximum number of animations to load.
 - Fixed a few other small errors that could occur in weird cases such as for some descriptors.

**NOTE**: This is the final Blender 2.79 compatible release. All future releases will be for Blender 2.80 and above.

### v0.9.17 (28/08/2019)

 - Fixed the issue where adding the addon from a zip file wouldn't actually add it to blender.
 - NMSDK can now also be run on blender on linux, however MBINCompiler doesn't work on this platform so it has limited uses...

### v0.9.16 (20/08/2019)

 - Quick fix to implement compatibility with new Beyond-style scenes.

### v0.9.15 (13/08/2019)

 - Mostly internal updates. Made some changes to the internal API and added a new public function for exporting models via the command line. More information can be found on the [API guide](api.md) page.

### v0.9.14 (10/08/2019)

 - The animation exporting system has received a major overhaul. It is now far mor easy for each part to have mutliple animations.
 - The Idle animation can now be set from the `Animation controls` section of the NMSDK toolbar. Any animation that isn't specified as the idle one 

#### v0.9.13 (02/08/2019)

 - Import process has been expanded to allow for animations to be imported. This includes both simple animations (one with just translation/rotation/scaling of nodes in the scene), as well as complex animations which involve skinned meshes and bones. Currently complex animations are still a bit broken, but hopefully they will be fixed in the future.
 To see more details on what options are available for imported animations, see [here](importing/importing.md#import_settings).
 - Tests have been added to NMSDK! This has no affect on the plugin itself, however if you clone the repo from github you will now notice a number of files from the game which are used to test the importing capabilities of NMSDK. This will be extended greatly in the future, but for now there is only the framework and a few simple tests.

#### v0.9.12 (03/06/2019):

- Add support for importing `Box`, `Cylinder` and `Sphere` type primitive collisions.
- On import there is an option to allow for displaying the collisions which is false by default.
- Display of collisions can be toggled by the button in the NMSDK side panel.
- When importing models, importing collisions can be turned off so that no collision meshes appear in the scene.
- Default values can be set for the `export path` and `group name` export properties in the NMSDK settings panel. These will persists across multiple sessions to make exporting multiple models in the same set easier.

#### v0.9.11 (25/05/2019):

- This version (FINALLY!) implements the exporting of mesh type collisions.

To allow this the `Mesh` type has been re-enabled in the `Collision` node panel.
Currently if you wish to export a mesh type collision, you need to apply the scale and rotation transforms to the mesh, otherwise your exported data will not have these values.

#### v0.9.10 (24/05/2019):

- This version fixes a number of issues introduced in v0.9.9 when attempting to fix imports. Exports should now be far more stable.

#### v0.9.9 (23/05/2019):

- Vertex colour is now able to be exported. To add vertex colour to a model change the mode in blender to "Vertex Paint".
- Nested referenced scenes can also be exported. This gives complete flexibility to the way a scene is to be exported.
