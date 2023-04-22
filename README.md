it's the atempt to run this jupyter notebook in a Docker container   

just download it and start the containers    
- docker composer up -d --build  

container -notebook serves port 8888    
acces it by http://localhost:8888/  

Step 1..4 wok fine in container -notebook    

Step 5,6 run in container -py  (port 5000,8050)   
it is part of the initial build   
app.py is started as initial application.   
there is no error message anyhow http://localhost:5000/

for step 6.  
manually start 
- docker-compose exec -it py python3 expdash.py   
  
it listens and reacts to http://localhost:8050/   
but the result is not as expected.   
could be some more modules arre required. 

I'm done. and stop my experiments.   
