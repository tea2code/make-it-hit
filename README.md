# Make It Hit

A little game where you must shoot objects to targets.

## Changelog

- [2013-02-23] Version 1: Basically a improved version of the prototype. Better map/level format with improved parser.
- [2013-04-03] Version 2: Fixed window size with scaling of level. In game menu and main menu with level selection.
- [2013-04-21] Version 3: Replacement of xml with yaml as level format. Configuration module. Gravitational force (positive and negative).

## Roadmap

**DISCONTINUED...**

- [?] Version 4: Sound. New level features (reflection and collision as an attribute of objects).
- [?] Version 5: Highscores. New level features (maybe triangle as an object). Possible first public version.
- [?] Version 6: Graphic themes. PyQt as rendering base. New level features.

## Known Bugs:

- Collision detection can fail (for example with high speed) so that the player enters objects.
- After colliding the player moves along the edge of the object. Probably same as above.

## Points

### Plus Points:
- Every target gives a specific amount of points. 
- Every bumb with an object or the border gives two points.
- And for every second left you get 5 points (fractions are calculated).

### Minus Points:

- Currently nothing.

## Level Format
 
The level format uses YAML files. Please read [wikipeda.org](http://en.wikipedia.org/wiki/Yaml) and [yaml.org](http://yaml.org/) for further information.

If not mentioned otherwise all values are strings. Integer, floating-point or boolean values are marked. A level without all required values might not work at all.

As this game is developed the map parser will evolve. Changes (added and removed features) will be marked. You should always stay compatible with the current version. Compatibility with older versions is possible but not certain.

Current Version: **3**

### Map Elements
 
#### Level

- author -- The author. Default empty.
- date -- Date of last update. Default empty.
- description -- A brief description. Default empty.
- map -- The map. See below. Required.
- name -- The name. Required.
- parser -- The parser version for this map. You should always use the newest (see above). Integer. Required.
- timelimit -- The time limit to solve the level in milliseconds. Integer. Required.
- version -- The version. Default empty.
 
#### Map

- border -- The width of the border. Integer. Required.
- height -- The height of the map. Integer. Required.
- objects -- List of objects. See below. Required but can be empty.
- player -- The player. See below. Required.
- targets -- List of targets. See below. Required.
- width -- The width of the map. Integer. Required.
 
#### Player

The player must always have a mass unequal zero. If it is set to zero it will be overriden with 1. The player mass affects how all/most of the forces act. A negative mass will invert most of the forces.
The attribute "colliding" has no effect on the player object.

- *object* -- The player object. See below. Currently only circles are supported. Required.
 
#### Target

The attribute "colliding" is by default set to false for targets. If you set it to true other objects can collide with it. Useful in combination with "final" set to false.

- final -- If set to true the level ends if this target is hit. If set to false the level continues. Default true. Boolean
- *object* -- The target object. See below. Required.
- points -- Number of points received if hitting this target. Integer. Required.

#### Object

Every object has the following attributes:

- colliding -- If set to true other objects can collide with this object. If set to false another object would go through. Default true. Boolean.
- mass -- The mass of the object. Read chapter "Force". Default 0. Integer.
- x -- The x-component of the center. Integer. Required.
- y -- The y-component of the center. Integer. Required.
 
##### Circle

- radius -- The radius of the circle. Integer. Required.

##### Rect(angle)

- angle -- The angle of the rectangle. Float. Required.
- height -- The height of the rectangle. Integer. Required.
- width -- The width of the rectangle. Integer. Required.

### Force

The following description applies only if the player object has a positive mass. If it has a negativ mass all directions are inverted. If it has zero mass nothing happens. If an object has a mass it attracts the player object with a positive force. If the mass is negative it repulses the player with a negativ force. 