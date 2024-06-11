+++ 
date = 2024-05-31T23:48:00Z 
slug = "sea_angels" 
title = "Making Sea Angels: A Journey of Light, Art, and Technology" 
+++

![](/uploads/container.JPEG)

The Sea Angels project is a labor of love. Lighthouses have always fascinated me. They provide direction, security, and solitude. I make it a point to visit a lighthouse wherever I travel. For EMF 2024, I decided to create a project that pays tribute to these beacons while also honouring the memory of my cat Bobble, who sadly passed away during the pandemic. I didn't get the chance to say goodbye to Bobble, but he remains a bright light in my heart. This project is dedicated to him.

#### The Concept:
The idea behind Sea Angels was to create a large-scale, living art piece that would showcase the global network of lighthouses. I created a 2m by 1.7m board with a 3D printed world map with topographical details, and then added LED lights around each country's coastline to represent real-world lighthouses. Each LED would have its own unique flashing pattern, mimicking the characteristics of the actual lighthouse it represents.

#### Data Gathering and Processing:
To begin, the data on the characteristics of lighthouses worldwide was gathered, including their on/off patterns, geogaphical locations, range, and colours. With this data in hand, I applied machine learning clustering algorithms to select a representative subset of 188 lighthouses, ensuring a balanced geographical distribution while considering factors such as proximity and brightness. You can see the detailed map of lighthouses here.

![](/uploads/full_map.JPEG)

#### Electronics and Power Management
One of the biggest challenges in this project was powering and controlling the 188 LEDs individually using three Arduino Uno boards. After extensive research and experimentation, I settled on using 5V SK6812  RGBW LED strips with 144 lights per meter. My original idea was to cut them into individual lights and reconnect them using wires to achieve the desired curves around the coastlines. This turns out to be a very slow process and with lots of room for errors given the tiny plates of the LED lights for soldering. I eventually settled on using end emitting 2mm fibre optics to direct the lights (more on that later).

To manage the power and control aspects, I divided the back board into two 100cm*170cm pieces, and the LED strips into three sections, each accommodating around 50  to 75 LED lights. This segmentation allowed for more efficient power management, fewer failure points, and simpler wiring process. I've also added a 1000mf, 6.3v capacitor to each LED strip to prevent initial power surges from damaging LEDs when they are turned on. The set up is to ensure the final piece is as robust as possible.

![](/uploads/resin_back.JPEG)

#### Printing the 3D Map

Creating the 3D topographically accurate map of the world was a time-consuming process. I have a Bambu X1C  printer which turned out to be very well suited to this task. For the 3D models, I am grateful to KamSav's generous sharing of the elevated 3D world map models on MakerWorld. I've also spent countless hours to ensure that each country fit together seamlessly with a modified projection method. Some countries, like Canada and China, which have more complex border shapes, required multiple attempts to get the perfect fit. One thing I didn't quite appreciate is that even with the same manufacturer the same "white" PLA filament could have a slightly different shade of white in real life. 

![](/uploads/map_partial.JPEG)

#### Assembly and Finishing Touches

With the 3D printed map and electronics in place, I began the meticulous process of assembling the piece. I chose a novel background material of 9mm jigsaw felt boards representing the puzzling world in which lighthouses are beacons of directions. The felt boards are attached to a 3mm cardboard for structural stability.  I then started drilling holes for the fibre optics, annotating each lighthouse identifier on the back of the cardboards, and positioning the LED strips to the back of the map.

After a few tries of various attaching method, I settled on using the UV resin which achieves both sturdiness and speed to attach end emitting fibre optic cables to individual LED light. Once the connections were secure, I carefully poked each fiber optic through the drilled holes, locking them in place to create the illusion of glowing coastlines. 2mm fibre optics are quite rigid, hot air gun was used to soften them to achieved the desired bend.

![](/uploads/electronics.JPEG)

#### The Final Result
After two months of hard work, Sea Angels finally came to life. Creating Sea Angels was a journey through data analysis, electronic engineering, precision crafting, and artistic expression. The result is a soothing art installation that showcases the beauty and importance of lighthouses worldwide. As viewers approach the piece, they are greeted by the gentle glow of the LEDs, each flashing in its own unique pattern, creating a mesmerising dance of light that tells the story of these guiding beacons.

![](/uploads/lighthouses_5fps.gif)

The making of Sea Angels has been an incredible journey of learning, experimentation, and perseverance. I hope that this project inspires other makers and artists to undertake your projects, no matter how complex they may seem at the start. Each piece of art starts with a single step—or in this case, a single light.
