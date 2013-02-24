# Make It Hit

A little game where you must shoot objects to targets.

## Changelog

- [2012-02-23] Version 1: Basically a improved version of the prototype. Better map/level format with improved parser.

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
 
If not mentioned otherwise all values are strings. Integer, floating-point or boolean values are marked. A level without all required values might not work at all.

As this game is developed the map parser will evolve. Changes (added and removed features) will be marked. You should always stay compatible with the current version.

Current Version: __1__
 
### Level

#### Attributes:
- parser -- The parser version for this map. You should always use the newest (see above). Integer. Required.

#### Elements:
- author -- The author. Default empty.
- date -- Date of last update. Default empty.
- description -- A brief description. Default empty.
- map -- The map. See below. Required.
- name -- The name. Required.
- timelimit -- The time limit to solve the level in milliseconds. Integer. Required.
- version -- The version. Default empty.
 
### Map

#### Elements:
- border -- The width of the border. Integer. Required.
- height -- The height of the map. Integer. Required.
- objects -- List of objects. See below. Required.
- player -- The player. See below. Required.
- targets -- List of targets. See below. Required.
- width -- The width of the map. Integer. Required.
 
### Player

#### Elements:
- *object* -- The player object. See below. Currently only circles are supported. Required.
 
### Target

### Elements:
- *object* -- The target object. See below. Required.
- points -- Number of points received if hitting this target. Integer. Required.
 
### Object: Circle

#### Elements:
- radius -- The radius of the circle. Integer. Required.
- x -- The x-component of the center. Integer. Required.
- y -- The y-component of the center. Integer. Required.
 
### Object: Rect(angle)

#### Elements:
- angle -- The angle of the rectangle. Float. Required.
- height -- The height of the rectangle. Integer. Required.
- width -- The width of the rectangle. Integer. Required.
- x -- The x-component of the center. Integer. Required.
- y -- The y-component of the center. Integer. Required.