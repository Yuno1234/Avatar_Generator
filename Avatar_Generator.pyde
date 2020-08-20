size(500, 500)
background('#e2e3d8')

translate(width/2, height/2)

r = random(225)
gr = random(225)
b = random(225)

fill(r+80, gr+80, b+80)
noStroke()
circle(0,0, 195)

for a in range(2,10):

    g = random(225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, PI+PI/2)
    noFill()
    stroke(r, g, b)
    strokeWeight(15)
    arc(0,0, 20*a,20*a, bg,ed)
    
    g = random(225)
    bg = random(0, 2*PI)
    ed = bg + random(PI, PI+PI/2)
    noFill()
    stroke(r, g, b)
    strokeWeight(7)
    arc(0,0, 20*a,20*a, bg,ed)
    
