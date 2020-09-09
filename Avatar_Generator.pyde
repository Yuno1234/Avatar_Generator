firstname = "Yunosuke"
lastname = "Arakawa"
username = "YUNO123"
sum_deb = 0

for letter in firstname and lastname and username:
    sum_deb += ord(letter)
    
seed = sum_deb
randomSeed(seed)



size(500, 500)
background('#e2e3d8')
translate(width/2, height/2)



# circle_L

# radius of the circle
circle_r = 170
# center of the circle (x, y)
circle_x = 0
circle_y = 0

# random angle
theta_L = 2 * PI * random(0, 1)
# random radius
r = circle_r * random(0.9, 1)
# calculating coordinates
x = r * cos(theta_L) + circle_x
y = r * sin(theta_L) + circle_y

r = random(50,225)
g_b = random(50,225)
b = random(50,225)

fill(r+80, g_b+80, b+80)
noStroke()
circle(x,y, 650)
    
for a in range(2,20):

    g = random(50,225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, 2*PI)
    noFill()
    stroke(r, g, b)
    strokeWeight(30)
    arc(x,y, 30*a,30*a, bg,ed)

    g = random(50,225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, 2*PI)
    noFill()
    stroke(r, g, b)
    strokeWeight(50)
    arc(x,y, 30*a,30*a, bg,ed)



# circle_M

# radius of the circle
circle_r = 170
# center of the circle (x, y)
circle_x = 0
circle_y = 0

# random angle
theta = 2 * PI * random(0, 1)
# random radius
r = circle_r * random(0.8, 1)
# calculating coordinates
x = r * cos(theta) + circle_x
y = r * sin(theta) + circle_y

r = random(50,225)
g_b = random(50,225)
b = random(50,225)

fill(r+80, g_b+80, b+80)
noStroke()
circle(x,y, 270)
    
for a in range(1,11):

    g = random(50,225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, 2*PI)
    noFill()
    stroke(r, g, b)
    strokeWeight(20)
    arc(x,y, 25*a,25*a, bg,ed)

    g = random(50,225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, 2*PI)
    noFill()
    stroke(r, g, b)
    strokeWeight(10)
    arc(x,y, 25*a,25*a, bg,ed)



# circle_S

# radius of the circle
circle_r = 150
# center of the circle (x, y)
circle_x = 0
circle_y = 0

# random angle
theta = theta + 2 * PI * random(0.25, 0.75)
# random radius
r = circle_r * random(0.5, 1)
# calculating coordinates
x = r * cos(theta) + circle_x
y = r * sin(theta) + circle_y

r = random(225)
g_b = random(225)
b = random(225)

fill(r+80, g_b+80, b+80)
noStroke()
circle(x,y, 195)
    
for a in range(1,10):

    g = random(225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, 2*PI)
    noFill()
    stroke(r, g, b)
    strokeWeight(15)
    arc(x,y, 20*a,20*a, bg,ed)

    g = random(225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, 2*PI)
    noFill()
    stroke(r, g, b)
    strokeWeight(7)
    arc(x,y, 20*a,20*a, bg,ed)





# mask
fill('#e2e3d8')
noStroke()
beginShape()
vertex(-width/2,-height/2)
vertex(-width/2,height/2)
vertex(width/2,height/2)
vertex(width/2,-height/2)
beginContour()
vertex(-125,0)
bezierVertex(-125,-70, -70,-125, 0,-125)
bezierVertex(70,-125, 125,-70, 125,0)
bezierVertex(125,70, 70,125, 0,125)
bezierVertex(-70,125, -125,70, -125,0)
endContour()
endShape()




'''
strokeWeight(1)
circle(0, 0, 250)


# radius of the circle
circle_r = 200
# center of the circle (x, y)
circle_x = 0
circle_y = 0

for i in range(1000):
    # random angle
    theta = 2 * PI *random(0,1)
    # random radius
    r = circle_r * random(0.5, 1)
    # calculating coordinates
    x = r * cos(theta) + circle_x
    y = r * sin(theta) + circle_y
    
    circle(x,y, 10)
'''
