#python -m pip install pypng
import png
import math

from Frame import Frame
from Ray import Ray
from Point3D import Point3D
from AreaLight import AreaLight
from Camera import Camera
from Color import Color
from DirectionalLight import DirectionalLight
from Light import Light
from Material import Material
from OrthographicCamera import OrthographicCamera
from PerspectiveCamera import PerspectiveCamera
from PointLight import PointLight
from SceneObject import SceneObject
from Sphere import Sphere
from SpotLight import SpotLight





print("Starting our ray tracer")

frame = Frame(256, 256)
    
directionalLightX = 0
directionalLightY = -1
directionalLightZ = 0

for y in range(256):
    for x in range(256):
        # Pattern to move between reference spaces
        # 1. Divide by maximum value
        # 2. Subtract by .5 so I'm center about 0
        # 3. Mltiply by the biggest number in the new space
        cameraX = x/255 #1.
        cameraX = cameraX - .5 #2.
        cameraX = cameraX * 2 #3.

        cameraY = y/255
        cameraY = cameraY - .5
        cameraY = cameraY * 2
        cameraY = cameraY * -1 # Account for flipped Y

        pixelX = cameraX # Just because we set it up right
        pixelY = cameraY
        pixelZ = 0

        originX = 0
        originY = 0
        originZ = 1

        sadDirectionX = pixelX - originX
        sadDirectionY = pixelY - originY
        sadDirectionZ = pixelZ - originZ

        lengthSad = math.sqrt(sadDirectionX*sadDirectionX + sadDirectionY*sadDirectionY + sadDirectionZ*sadDirectionZ)

        directionX = sadDirectionX / lengthSad
        directionY = sadDirectionY / lengthSad
        directionZ = sadDirectionZ / lengthSad

        origin = Point3D(originX, originY, originZ)
        direction = Point3D(directionX, directionY, directionZ)
        center = Point3D(0,0,0)
        radius = .5

        e = origin.minus(center)
        a = direction.dot(direction)
        b = 2*direction.dot(e)
        c = e.dot(e)-radius*radius

        discriminant = b*b - 4 * a * c
        if disriminant < 0
            frame.buffer[y*256*3+x*3] = 0
            frame.buffer[y*256*3+1+x*3] = 0
            frame.buffer[y*256*3+2+x*3] = 0
        
        else:
            optionA = (-b - math.sqrt(discriminant))/(2*a)
            optionB = (-b + math.sqrt(discriminant))/(2*a)

            t = -1
            if optionA < 0 and optionB < 0:
                t = optionB
            elif optionA >= 0:
                t = optionA
            else:
                t = optionB

            if t < 0
                frame.buffer[y*256*3+x*3] = 0
                frame.buffer[y*256*3+1+x*3] = 0
                frame.buffer[y*256*3+2+x*3] = 0
            else:
                ambient = 10
                diffuse = 0
                specular = 0

                # I need the normal
                # I need the light direction
                # I need a dot product

                collisionX = directionX * t + originX
                collisionX = directionY * t + originY
                collisionX = directionZ * t + originZ

                uNNx = collisionX - center.x
                uNNy = collisionY - center.y
                uNNz = collisionZ - center.z

                normalLength = math.sqrt(uNNx**2 + uNNy**2 + uNNz**2)
                circleNormalX = uNNx / normalLength
                circleNormalY = uNNy / normalLength
                circleNormalZ = uNNz / normalLength

                collisionAngle = math.atan2(circleNormalY, circleNormalX)
                collisionAngle2 = math.atan2(circleNormalX, circleNormalZ)

                toLightX = -directionalLightX
                toLightY = -directionalLightY
                toLightZ = -directionalLightZ

                dotProduct = circleNormalX * toLightX + circleNormalY * toLightY + circleNormalZ + toLightZ
                if doProduct < 0:
                    dotProduct = 0

                if (math.floor(collisionAngle * 100) % 2 == 0):
                    dotProduct = 0

                diffuseR = 255 * dotProduct
                diffuseG = 255 * dotProduct
                diffuseB = 255 * dotProduct

                cR = math.floor(ambient + diffuseR + specular)
                cG = math.floor(ambient + diffuseG + specular)
                cB = math.floor(ambient + diffuseB + specular)
                
                if cR > 255:
                    cR = 255
                if cG > 255:
                    cG = 255
                if cB > 255:
                    cB = 255

                frame.buffer[y*256*3+x*3] = cR
                frame.buffer[y*256*3+x*3+1] = cG
                frame.buffer[y*256*3+x*3+2] = cB

##Write the buffer out to a file

#Open the output file in binary mode
f = open('./saved.png', 'wb')

#Create a write object
w = png.Writer(frame.width, frame.height, greyscale=False)

#Write to the open file
w.write_array(f, frame.buffer)

#Close the file
f.close()

print("Finished rendering the file")