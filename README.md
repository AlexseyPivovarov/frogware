**Requirements**    
Python 3.6, 3.7


**Install**
```
pip3 install django
git clone https://github.com/AlexseyPivovarov/frogware
cd frogware
python manage.py migrate
```




**Run application:**
```
python manage.py runserver :8080
```
**Usage:**

Available Endponits:

- GET /   
    Download main page html
- GET /detail/\<str:alias>\<int:globalId>       
    Download detail html
    > alias - quest alias    
     globalId - quest globalId
   
- POST /api/        
    Upload FinishedQuestsLeafs.json     
    > Body: \<File content>




   
   
      